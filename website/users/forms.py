from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from website.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    profile_image = FileField('Update Profile Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    update = SubmitField('Update Profile')


    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Duplicate username')


class BackgroundForm(FlaskForm):
    
    background = FileField('Update Background Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    change_background = SubmitField('Change Background')


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('confirm_password', message="Password must be the same!")])
    change_password = SubmitField('Change Password')

