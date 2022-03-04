# Must do: pip install wtforms & pip install email_validator

from wtforms import Form, BooleanField,StringField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField
from wtforms.fields import TextAreaField, HiddenField

class StudentForm(Form):
    givenName = StringField('First name', validators=[DataRequired()])
    lastName = StringField('Last name', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired(), Email(), Length(max=120)])
    studyProgram = TextAreaField('Study program', [validators.Length(min=6, max=500)])
    id = HiddenField()
    submit = SubmitField('Update')
    #password = PasswordField('New Password', [
    #    validators.InputRequired(),
    #    validators.EqualTo('confirm', message='Passwords must match')
    #])
    #confirm = PasswordField('Repeat Password')
    #accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
    #                          [validators.InputRequired()])