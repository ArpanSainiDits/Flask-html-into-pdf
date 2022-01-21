from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



UPLOAD_FOLDER = '/media'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/pdf'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

