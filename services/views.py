from flask_restful import Resource
import pdfkit
from flask import render_template, make_response, request

from models.pdf import *

from db import db

class htmlPdf(Resource):
    
    def post(self, name, location):
        file = request.json['file']
        
        profile = Profile(file)
        db.session.add(profile)
        db.session.commit()
        print("---------->", profile)
        
        rendered = render_template('a.html', name=name, location=location)
        pdf = pdfkit.from_string(rendered, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
        return response
