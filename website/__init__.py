import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__)


app.config['SECRET_KEY'] = "437018557f77ba29b4aaae36305602747b2cbf04"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = datetime.timedelta(minutes=15)

db = SQLAlchemy(app)
Migrate(app, db)


login_manager = LoginManager()
login_manager.session_protection = "strong"


login_manager.init_app(app)
login_manager.login_view = 'users.login'

from website.articles.views import articles
from website.users.views import users
from website.error.error_handler import error_pages
from website.core.views import core

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(articles)
