import pdfkit
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/pdf'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

config = pdfkit.configuration(
    wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")

# pdfkit.from_url('http://google.com', 'out.pdf', configuration=config)
pdfkit.from_file('a.html', 'out.pdf', configuration=config)
# pdfkit.from_string('Hello!', 'out.pdf', configuration=config)


if __name__ == "__main__":
    app.run(debug=True)
