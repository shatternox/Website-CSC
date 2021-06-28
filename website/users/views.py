from flask import render_template, Blueprint, url_for, flash, request, redirect, session, abort
from flask_login import login_user, current_user, logout_user, login_required
from website import db, app
from website.models import User, ToDoList
from website.users.forms import LoginForm, UpdateAccountForm, BackgroundForm, ChangePasswordForm
from website.todo.forms import ToDoForm, ToDoUpdate
from website.users.pic_handler import save_profile_image, save_background_image
from datetime import timedelta, datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
users = Blueprint('users', __name__)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data):

            login_user(user)

            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=15)

            flash("Login Success")

            next = request.args.get('next')

            if next == None or next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form, title='Login')


@users.route("/user/<username>", methods=['GET', 'POST'])
@login_required
def account(username):
    user = User.query.filter_by(username=username).first()
    if user == None:
        abort(404)

    ############################################################################
    ############################## UPDATE ACCOUNT ##############################
    ############################################################################

    form = UpdateAccountForm()
    user = User.query.filter_by(username=username).first()
    if form.validate_on_submit():

        user = User.query.filter_by(username=username).first()
        if form.profile_image.data:
            picture = save_profile_image(
                form.profile_image.data, user.profile_image)
            user.profile_image = picture

        if '/' in form.username.data or '\\' in form.username.data:
            pass
        else:
            user.username = form.username.data
            user.email = form.email.data

        db.session.commit()

        return redirect(url_for('users.account', username=user.username))

    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email

    ############################################################################
    ############################## CHANGE PASSWORD #############################
    ############################################################################
    form_password = ChangePasswordForm()

    if form_password.validate_on_submit() and form_password.change_password.data:
        user = User.query.filter_by(username=username).first()

        if user.check_password(form_password.current_password.data):
            current_user.password_hash = bcrypt.generate_password_hash(
                form_password.new_password.data)
            flash('Password Has Been Change', 'info')
            db.session.commit()

        else:
            flash('Please enter data correctly!', 'info')

    ############################################################################
    ############################### CREATE TODO ################################
    ############################################################################
    form_todo = ToDoForm()

    if form_todo.validate_on_submit() and form_todo.submit.data:
        user = User.query.filter_by(username=username).first()

        todo = ToDoList(title=form_todo.title.data,
                        text=form_todo.text.data, user_id=user.id)

        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('users.account', username=user.username))

    ############################################################################
    ############################## UPDATE TODO #################################
    ############################################################################
    form_toupdate = ToDoUpdate()

    if form_toupdate.update.data:

        user = User.query.filter_by(username=username).first()
        todo = ToDoList.query.get_or_404(form_toupdate.todo_id.data)

        if todo.author == current_user or (current_user.role == 2 or current_user.role == 3):

            todo.title = form_toupdate.title.data
            todo.text = form_toupdate.text.data
            db.session.commit()

        else:
            abort(403)

    ############################################################################
    ############################## DELETE TODO #################################
    ############################################################################

    if form_toupdate.delete.data:

        user = User.query.filter_by(username=username).first()
        todo = ToDoList.query.get_or_404(form_toupdate.todo_id.data)

        if todo.author == current_user or (current_user.role == 2 or current_user.role == 3):
            db.session.delete(todo)
            db.session.commit()
        else:
            abort(403)

    ############################################################################
    ############################ CHANGE BACKGROUND #############################
    ############################################################################

    form_background = BackgroundForm()
    if form_background.background.data:
        user = User.query.filter_by(username=username).first()
        if form_background.background.data:
            picture = save_background_image(
                form_background.background.data, user.background)

            user.background = picture

        db.session.commit()

        return redirect(url_for('users.account', username=user.username))

    todo_list = ToDoList.query.filter_by(
        user_id=user.id).order_by(ToDoList.date.desc())

    return render_template('account.html', title='Account', form=form, todo=todo_list, form_todo=form_todo, user=user, form_toupdate=form_toupdate, form_background=form_background, form_password=form_password)
