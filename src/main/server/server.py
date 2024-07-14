"""
Este módulo é um aplicativo Flask básico.
"""

from flask import Flask
from src.main.routes.trips_routes import trips_route_bp
app = Flask(__name__)

app.register_blueprint(trips_route_bp)