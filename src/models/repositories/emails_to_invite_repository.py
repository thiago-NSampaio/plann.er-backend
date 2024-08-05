from sqlalchemy.orm import Session
from src.models.settings.initDB import EmailToInvite


class EmailsToInviteRepository:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def registry_email(self, emails_infos: dict) -> None:
        new_email = EmailToInvite(
            id=emails_infos["id"],
            trip_id=emails_infos["trip_id"],
            email=emails_infos["email"],
        )
        self.__session.add(new_email)
        self.__session.commit()

    def find_emails_from_trip(self, tripId: str) -> list[tuple]:
        return self.__session.query(EmailToInvite).filter_by(trip_id=tripId).all()
