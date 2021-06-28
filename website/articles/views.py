from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from website import db, app
from website.models import Article
from website.articles.forms import ArticleForm
from website.articles.pic_handler import save_article_image

articles = Blueprint('articles', __name__)

# CREATE


@articles.route('/article/create', methods=['GET', 'POST'])
@login_required
def create_article():
    form = ArticleForm()

    if form.validate_on_submit():

        article = Article(title=form.title.data,
                          content=form.content.data, user_id=current_user.id)
        db.session.add(article)
        db.session.commit()

        if form.picture.data:
            picture = save_article_image(
                form.picture.data, article.picture)
            article.picture = picture

        db.session.commit()
        return redirect(url_for('articles.article'))

    return render_template('create_article.html', form=form)

# READ


@articles.route('/article/<int:article_id>')
def article_solo(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article_solo.html', article=article)


# UPDATE
@articles.route('/article/update/<int:article_id>', methods=['GET', 'POST'])
@login_required
def update_article(article_id):
    article = Article.query.get_or_404(article_id)

    if article.author != current_user:
        abort(403)

    form = ArticleForm()

    if form.validate_on_submit():
        article.title = form.title.data
        article.content = form.content.data
        db.session.commit()

        if form.picture.data:
            picture = save_article_image(
                form.picture.data, article.picture)
            article.picture = picture
        db.session.commit()

        return redirect(url_for('articles.article', article_id=article.id))

    elif request.method == 'GET':
        article = Article.query.get_or_404(article_id)
        form.title.data = article.title
        form.content.data = article.content

    return render_template('create_article.html', form=form)

# DELETE


@articles.route('/article/delete/<int:article_id>', methods=['GET', 'POST'])
@login_required
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)

    if article.author != current_user:
        abort(403)

    db.session.delete(article)
    db.session.commit()

    return redirect(url_for('articles.article'))


@articles.route('/article')
def article():
    page = request.args.get('page', 1, type=int)
    article = Article.query.order_by(
        Article.date.desc()).paginate(page=page, per_page=3)

    return render_template('article.html', article=article)
