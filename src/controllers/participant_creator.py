import uuid
import logging

class ParticipantCreator:
    def __init__(self, participants_repository, emails_repository) -> None:
        self.__participant_repository = participants_repository
        self.__emails_repository = emails_repository

    def create(self, body, tripId) -> dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_infos = {
                "email": body["email"],
                "id": email_id,
                "trip_id": tripId,
            }

            participants_infos = {
                "id": participant_id,
                "trip_id": tripId,
                "emails_to_invite_id": email_id,
                "name": body["name"]
            }

            self.__emails_repository.registry_email(emails_infos)
            self.__participant_repository.registry_participant(participants_infos)

            return {
                "body": {"participant_id": participant_id},
                "status_code": 201
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400
            }
