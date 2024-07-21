class ParticipantFinder():
    def __init__(self,participants_repository) -> None:
        self.__participants_repository = participants_repository

    def finder(self, tripId) -> dict:
        try:
            participants = self.__participants_repository.find_participants_from_trip(tripId)
            formmated_participants = []
            for participant in participants:
                formmated_participants.append({
                    "id": participant[0],
                    "name": participant[1],
                    "is_confirmed": participant[2],
                    "email": participant[3]
                })

            return {
                "body":{"participants":formmated_participants},
                "status_code": 200
            }

        except Exception as e:
            return {
                "body":{"error":"Bad Request", "message": str(e)},
                "status_code": 400
            }