class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository
    
    def finder(self,tripId) -> dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(tripId)
            formmated_activity = []

            for activity in activities:
                formmated_activity.append({
                    "id":activity[0],
                    "trip_id": activity[1],
                    "title": activity[2],
                    "occurs_at":activity[3]
                })

            return {
                "body":{"activities":{formmated_activity}},
                "status_code": 200
            }
        except Exception as e:
            return{
                "body":{"error": "Bad Request", "message": str(e),
                "status_code":400}
            }