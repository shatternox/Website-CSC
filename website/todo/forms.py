from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired


class ToDoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Create Todo')


class ToDoUpdate(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])
    todo_id = HiddenField('Todo ID', validators=[DataRequired()])
    delete = SubmitField('Delete Todo')
    update = SubmitField('Update Todo')