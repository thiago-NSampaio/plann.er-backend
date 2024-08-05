"""Rotas da api"""
from src.models.settings.db_connection_handler import DBConnectionHandler

from flask import jsonify, Blueprint, request
# importação de Repositórios
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

# importação de Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.trip_update import TripUpdate

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.controllers.participant_delete import ParticipantDelete

from src.controllers.activity_finder import ActivityFinder
from src.controllers.activity_creator import ActivityCreator

trips_route_bp = Blueprint("trips_routes", __name__)


@trips_route_bp.route("/trips", methods=["POST"])
def create_trip():
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    trips_repository = TripsRepository(session)
    emails_repository = EmailsToInviteRepository(session)

    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    trips_repository = TripsRepository(session)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def update_trip_status(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    trips_repository = TripsRepository(session)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_link(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    links_repository = LinksRepository(session)
    controller = LinkFinder(links_repository)

    response = controller.finder(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_link(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    links_repository = LinksRepository(session)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    participants_repository = ParticipantsRepository(session)
    emails_repository = EmailsToInviteRepository(session)

    controller = ParticipantCreator(
        participants_repository, emails_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    activities_repository = ActivitiesRepository(session)

    controller = ActivityCreator(activities_repository)

    print(request.json)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    participants_repository = ParticipantsRepository(session)

    controller = ParticipantFinder(participants_repository)

    response = controller.finder(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<participantId>/confirm", methods=["PATCH"])
def confirm_participants(participantId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    participants_repository = ParticipantsRepository(session)

    controller = ParticipantConfirmer(participants_repository)

    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    activities_repository = ActivitiesRepository(session)

    controller = ActivityFinder(activities_repository)

    response = controller.finder(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>", methods=["PUT"])
def trip_update(tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    trips_repository = TripsRepository(session)

    controller = TripUpdate(trips_repository)

    response = controller.update(tripId, request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_route_bp.route("/trips/<tripId>/participants/<participantId>", methods=["DELETE"])
def delete_participant(participantId, tripId):
    db_handler = DBConnectionHandler()
    session = db_handler.get_connection()

    participants_repository = ParticipantsRepository(session)

    controller = ParticipantDelete(participants_repository)

    response = controller.delete(participantId, tripId)

    return jsonify(response["body"]), response["status_code"]
