from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '435klf44l60sqqer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead
# and will be disabled by default in the future
# Set it to True to suppress this warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from blog import routes