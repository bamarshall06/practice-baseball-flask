from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, DecimalField
from wtforms.validators import DataRequired


##### LOGIN FORM #####
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


##### TEAM FORM #####
class TeamForm(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired()])
    team_mascot = StringField('Team Mascot', validators=[DataRequired()])
    submit = SubmitField('Submit')

##### PRACTICE FORM #####
class PracticeForm(FlaskForm):
    practice_date = DateField('Practice Date', format='%Y-%m-%d', validators=[DataRequired()])
    practice_length = DecimalField('Practice Length')
    teams = SelectField('Teams', choices=[])
    submit = SubmitField('Submit')