import uuid

class ActivityCreator:
    def __init__(self,activities_repository) -> None:
        self.__activities_repository = activities_repository

    def create(self, body, tripId)-> dict:
        try:
            activity_id = str(uuid.uuid4())
            activities_infos = {
                "id": activity_id,
                "trip_id": tripId,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }
            print(activities_infos)

            self.__activities_repository.registry_activity(activities_infos)

            return {
                "body": {"activityId": activity_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body":{"error":"Bad Request", "message":str(exception)},
                "status_code": 400
            }