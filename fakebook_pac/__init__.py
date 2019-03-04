from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SECRET_KEY']='7c255f06115ede5bb8787d2ea01f4188'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fakebook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from fakebook_pac import routes #located here to avoid circular importing
