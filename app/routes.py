from flask import render_template, url_for, redirect, flash, session, request
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app import app, db
from app.models import User, Team, Practice
from app.forms import LoginForm, TeamForm, PracticeForm
from app.functions import *

#### LOGIN STUFF NEEDED
##### USER MANAGEMENT ##### FOUND: https://www.youtube.com/watch?v=2dEM-s3mRLE
login_manager = LoginManager()
login_manager.init_app(app)

# This method is used to as part of the flask_login code.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return  render_template('index.html')



### LOGIN LOGOUT STUFF ####

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    # get form data
    form_username = form.username.data
    form_password = form.password.data

    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form_username).first()
        password = user.password
        if user is None or password != form_password:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        session.permanent = True
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


###### TEAMS - ADD EDIT DELETE

#### ADD TEAM - READ TEAM
@app.route('/teams', methods=['GET', 'POST'])
@login_required
def teams():
    form = TeamForm()
    if request.method == 'POST':
        team_name = request.form.get('team_name')
        team_mascot = request.form.get('team_mascot')
        teams = Team(team_name=team_name, team_mascot=team_mascot)
        db.session.add(teams)
        db.session.commit()
        return redirect(url_for('teams'))
    teams = get_teams()
    return render_template('teams.html', form=form, teams=teams)

@app.route('/team_update/<team_id>/', methods=['GET', 'POST'])
@login_required
def team_update(team_id):
    team = Team.query.get(team_id)
    team.team_name = request.form.get('team_name')
    team.team_mascot = request.form.get('team_mascot')
    db.session.commit()
    flash(f"{team.team_name} has been udpated.")
    return redirect(url_for('teams'))

@app.route('/team_delete/<team_id>/', methods=['GET', 'POST'])
@login_required
def team_delete(team_id):
    db.session.query(Team).filter(Team.team_id==team_id).delete(synchronize_session='fetch')
    db.session.commit()
    flash(f"The team has been udpated.")
    return redirect(url_for('teams'))


#### ADD PRACTICE - READ PRACTICE
@app.route('/practices', methods=['GET', 'POST'])
@login_required
def practices():
    form = PracticeForm()

    teams = get_teams()

    form.teams.choices = [(team['team_id'], team['team_name']) for team in teams]

    if request.method == 'POST':
        practice_length = request.form.get('practice_length')
        practice_date = request.form.get('practice_date')
        team_id = request.form.get('teams')
        practices = Practice(practice_length=practice_length, practice_date=practice_date, team_id=team_id)
        db.session.add(practices)
        db.session.commit()
        return redirect(url_for('practices'))
    practices = get_practices()
    return render_template('practices.html', form=form, teams=teams, practices=practices)

@app.route('/practice_update/<practice_id>/', methods=['GET', 'POST'])
@login_required
def practice_update(practice_id):
    practice = Practice.query.get(practice_id)
    practice.practice_length = request.form.get('practice_length')
    practice.practice_date = request.form.get('practice_date')
    practice.team_id = request.form.get('teams')
    db.session.commit()
    flash(f"The pracitce has been udpated.")
    return redirect(url_for('practices'))

@app.route('/practice_delete/<practice_id>/', methods=['GET', 'POST'])
@login_required
def practice_delete(practice_id):
    db.session.query(Practice).filter(Practice.practice_id==practice_id).delete()
    db.session.commit()
    flash(f"The practice has been deleted.")
    return redirect(url_for('practices'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# This route redirects unauthrozied users to the login page.
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))