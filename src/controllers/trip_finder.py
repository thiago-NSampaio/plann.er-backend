from datetime import datetime


class TripFinder:
    def __init__(self, trips_repository):
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id):
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            return {
                "body": {
                    "trip": {
                        "id": trip.id,
                        "destination": trip.destination,
                        "start_date": trip.start_date,
                        "end_date": trip.end_date,
                        "owner_name": trip.owner_name,
                        "owner_email": trip.owner_email,
                        "status": trip.status
                    }
                },
                "status_code": 200
            }
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 404
            }
