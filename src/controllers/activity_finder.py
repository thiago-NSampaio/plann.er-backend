from collections import defaultdict

class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository
    
    def finder(self, tripId) -> dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(tripId)
            grouped_activities = defaultdict(list)

            for activity in activities:
                date = activity[3].split("T")[0] 
                grouped_activities[date].append({
                    "id": activity[0],
                    "trip_id": activity[1],
                    "title": activity[2],
                    "occurs_at": activity[3]
                })

            formatted_activity = [
                {"date": date, "activities": acts}
                for date, acts in grouped_activities.items()
            ]

            return {
                "body": {"activities": formatted_activity},
                "status_code": 200
            }
        except Exception as e:
            return {
                "body": { "error": "Bad Request", "message": str(e) },
                "status_code": 400
            }
