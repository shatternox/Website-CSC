from website import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
import datetime

bcrypt = Bcrypt()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# User Roles:
# 0 = Staff
# 1 = Koor
# 2 = DPI
# 3 = Webcreator


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    username = db.Column(db.String(128), unique=True,
                         index=True, nullable=False)
    role = db.Column(db.Integer, nullable=False, index=True)
    division = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128))
    profile_image = db.Column(
        db.String(100), nullable=False, default='default.png')
    background = db.Column(db.String(100), nullable=False,
                           default='default-bg.jpg')
    todo = db.relationship('ToDoList', backref='author', lazy=True)
    article = db.relationship('Article', backref='author', lazy=True)

    def __init__(self, email, name, username, division, password, profile_image, role):
        self.email = email
        self.name = name
        self.username = username
        self.division = division
        self.role = role
        self.profile_image = profile_image
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username: {self.username} Email: {self.email} Divisi: {self.division}"


class ToDoList(db.Model):

    __tablename__ = 'todolist'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.String, nullable=False,
                     default=datetime.datetime.utcnow().strftime('%d/%m/%Y'))
    title = db.Column(db.String(128), nullable=False, unique=True)
    text = db.Column(db.String(255), nullable=False, unique=True)
    done = db.Column(db.Boolean, nullable=False, default=0, unique=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"ToDoList: {self.id} Title: {self.Title} Date: {self.date}"


class Article(db.Model):

    __tablename__ = 'article'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.String, nullable=False,
                     default=datetime.datetime.utcnow().strftime('%d/%m/%Y'))
    title = db.Column(db.String(128), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False, unique=True)
    picture = db.Column(
        db.String(100), nullable=False, default='article.png')

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"Article: {self.id} Title: {self.Title} Date: {self.date}"
