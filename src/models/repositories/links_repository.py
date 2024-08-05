from sqlalchemy.orm import Session
from src.models.settings.initDB import Link


class LinksRepository:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def registry_link(self, links_info: dict) -> None:
        new_link = Link(
            id=links_info["id"],
            trip_id=links_info["trip_id"],
            link=links_info["link"],
            title=links_info["title"]
        )
        self.__session.add(new_link)
        self.__session.commit()
        self.__session.close()

    def find_links_from_trip(self, trip_id: str) -> list[Link]:
        if trip_id is None:
            raise ValueError("trip_id cannot be None")

        links = self.__session.query(Link).filter_by(trip_id=trip_id).all()

        if links is None:
            raise ValueError("Query result is None, expected a list")

        return links
