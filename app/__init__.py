from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

#database configuration
# each part of the connection is listed. The typical database on AWS is named sys.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@aws_server_host/database'

# create the database
db = SQLAlchemy(app)

# starting the login
login = LoginManager(app)


from app import routes, models


if __name__ == '__main__':
    app.run(debug=True)