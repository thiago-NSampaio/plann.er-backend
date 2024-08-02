class ParticipantDelete:
    def __init__(self,participants_repository) -> None:
        self.__participants_repository = participants_repository
    
    def delete(self,participantId,tripId) -> None:
        try:
            self.__participants_repository.delete_participant(participantId,tripId)
            return {"body":None,"status_code":204}
        except Exception as e:
               return {
                "body": { "error": "Bad Request", "message": str(e)},
                "status_code": 400
            }