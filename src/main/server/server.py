from flask_cors import CORS

from flask import Flask
from src.main.routes.trips_routes import trips_route_bp
app = Flask(__name__)
CORS(app)

app.register_blueprint(trips_route_bp)