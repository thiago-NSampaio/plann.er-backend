class ParticipantConfirmer:
    def __init__(self,participants_repository) -> None:
        self.__participants_repository = participants_repository
    
    def confirm(self,participantId) -> dict:
        try:
            self.__participants_repository.update_participant_status(participantId)
            return {"body":None,"status_code":204}
        except Exception as e:
            return{
                "body":{"error": "Bad Request", "message": str(e),
                "status_code":400}
            }
