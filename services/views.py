from flask_restful import Resource
import pdfkit
from flask import jsonify, request



from db import db

class htmlPdf(Resource):
    
    def post(self, fName):
        html = request.json.get('html')
        
        config = pdfkit.configuration(
            wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
        pdfkit.from_string(html, fName+".pdf", configuration=config)
        return jsonify({'status': 'Pdf successfully generated',
                        'click on this link for view': f"C:\projects\Flask html into pdf/{fName}.pdf"})
