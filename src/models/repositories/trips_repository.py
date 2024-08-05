from sqlalchemy.orm import Session
from src.models.settings.initDB import Trip
from datetime import datetime


class TripsRepository:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create_trip(self, trip_info: dict) -> None:
        trip_info["start_date"] = datetime.fromisoformat(
            trip_info["start_date"].replace("Z", "+00:00"))
        trip_info["end_date"] = datetime.fromisoformat(
            trip_info["end_date"].replace("Z", "+00:00"))

        new_trip = Trip(
            id=trip_info["id"],
            destination=trip_info["destination"],
            start_date=trip_info["start_date"],
            end_date=trip_info["end_date"],
            owner_name=trip_info["owner_name"],
            owner_email=trip_info["owner_email"],
            status=trip_info.get("status")
        )

        self.__session.add(new_trip)
        self.__session.commit()
        self.__session.close()

    def find_trip_by_id(self, trip_id: str) -> Trip:
        return self.__session.query(Trip).filter_by(id=trip_id).first()

    def update_trip_status(self, trip_id: str):
        self.__session.query(Trip).filter(
            Trip.id == trip_id).update({Trip.status: 1})
        self.__session.commit()
        self.__session.close()

    def upadate_trip(self, tripId: str, infos_trip_update: dict):
        self.__session.query(Trip).filter(Trip.id == tripId).update(
            {Trip.destination: infos_trip_update["destination"], Trip.start_date: datetime.fromisoformat(
                infos_trip_update["start_date"].replace("Z", "+00:00")), Trip.end_date: datetime.fromisoformat(
                infos_trip_update["end_date"].replace("Z", "+00:00"))})
        self.__session.commit()
        self.__session.close()
