from sqlalchemy.orm import Session
from src.models.settings.initDB import Activity
from datetime import datetime


class ActivitiesRepository:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def registry_activity(self, activities_infos: dict):
        occurs_at = datetime.fromisoformat(
            activities_infos["occurs_at"].replace("Z", "+00:00"))
        new_activity = Activity(
            id=activities_infos["id"],
            trip_id=activities_infos["trip_id"],
            title=activities_infos["title"],
            occurs_at=occurs_at
        )
        self.__session.add(new_activity)
        self.__session.commit()

    def find_activities_from_trip(self, trip_id: str) -> list[Activity]:
        activities = self.__session.query(
            Activity).filter_by(trip_id=trip_id).all()
        return activities
