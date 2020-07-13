from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class IDForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    submit = SubmitField('Enter')


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Enter')


class UpdateForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    user_id = IntegerField('User ID', validators=[DataRequired()])
    submit = SubmitField('Enter')


class MockForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    submit = SubmitField('Enter')