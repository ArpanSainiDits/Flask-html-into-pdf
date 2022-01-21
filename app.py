from flask import Flask
from routes import view_routes
from db import app




view_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
