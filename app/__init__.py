from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:pepsi2222@baseball.cqyhggbcdmue.us-east-1.rds.amazonaws.com/sys'

# create the database
db = SQLAlchemy(app)

# starting the login
login = LoginManager(app)


from app import routes, models


if __name__ == '__main__':
    app.run(debug=True)