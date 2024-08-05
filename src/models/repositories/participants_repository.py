from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.settings.initDB import Participant
from src.models.settings.initDB import EmailToInvite


class ParticipantsRepository:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def registry_participant(self, participant_infos: dict) -> None:

        participant = Participant(
            id=participant_infos["id"],
            trip_id=participant_infos["trip_id"],
            emails_to_invite_id=participant_infos["emails_to_invite_id"],
            name=participant_infos["name"]
        )
        self.__session.add(participant)
        self.__session.commit()

    def find_participants_from_trip(self, trip_id: str) -> list[tuple]:
        participants = (
            self.__session.query(
                Participant.id, Participant.name, Participant.is_confirmed, EmailToInvite.email)
            .join(EmailToInvite, EmailToInvite.id == Participant.emails_to_invite_id)
            .filter(Participant.trip_id == trip_id)
            .all()
        )
        return participants

    def update_participant_status(self, participant_id: str) -> None:
        self.__session.query(Participant).filter_by(
            id=participant_id).update({"is_confirmed": 1})
        self.__session.commit()

    def delete_participant(self, participant_id: str, trip_id: str) -> None:
        self.__session.query(Participant).filter_by(
            id=participant_id, trip_id=trip_id).delete()

        self.__session.commit()
        self.__session.rollback()
