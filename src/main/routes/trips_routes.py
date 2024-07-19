"""Rotas da api"""
from src.models.settings.db_connection_handler import db_connection_handler

from flask import jsonify, Blueprint,request
# importação de Repositórios
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository 
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.links_repository import LinksRepository

# importação de Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.link_creator import LinkCreator
from src.controllers.trip_confirmer import TripConfirmer

trips_route_bp = Blueprint("trips_routes", __name__)

@trips_route_bp.route("/trips",methods=["POST"])
def create_trip():
   conn =db_connection_handler.get_connection()
   trips_repository = TripsRepository(conn)
   emails_repository = EmailsToInviteRepository(conn)
   controller = TripCreator(trips_repository,emails_repository)

   response = controller.create(request.json)

   return jsonify(response["body"]), response["status_code"]

@trips_route_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
   conn =db_connection_handler.get_connection()
   trips_repository = TripsRepository(conn)
   controller = TripFinder(trips_repository)

   response = controller.find_trip_details(tripId)

   return jsonify(response["body"]), response["status_code"]

@trips_route_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def update_trip(tripId):
   conn =db_connection_handler.get_connection()
   trips_repository = TripsRepository(conn)
   controller = TripConfirmer(trips_repository)

   response = controller.confirm(tripId)

   return jsonify(response["body"]), response["status_code"]

@trips_route_bp.route("/trips/<tripId>/link", methods=["POST"])
def create_link(tripId):
   conn =db_connection_handler.get_connection()
   linksRepository = LinksRepository(conn)
   controller = LinkCreator(linksRepository)

   response = controller.create(request.json,tripId)

   return jsonify(response["body"]), response["status_code"]
