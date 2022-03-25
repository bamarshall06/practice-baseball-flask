from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app import app, db
from app.models import User, Team, Practice


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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))