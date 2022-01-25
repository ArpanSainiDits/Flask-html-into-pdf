from flask_restful import Api

from services.views import htmlPdf


def view_routes(app):
    api = Api(app)

    api.add_resource(htmlPdf, '/api/html/<fName>')
