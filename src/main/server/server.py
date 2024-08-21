from flask_cors import CORS

from flask import Flask
from src.main.routes.trips_routes import trips_route_bp
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*",
     "methods": ["GET", "POST", "PUT", "PATCH", "DELETE"]}})

app.register_blueprint(trips_route_bp)
