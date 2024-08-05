from datetime import datetime


class TripFinder:
    def __init__(self, trips_repository):
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id):
        trip = self.__trips_repository.find_trip_by_id(trip_id)
        if trip:
            return {
                "body": {
                    "trip": {
                        "id": trip.id,
                        "destination": trip.destination,
                        # Converte date para string no formato ISO
                        "start_date": trip.start_date.isoformat(),
                        # Converte date para string no formato ISO
                        "end_date": trip.end_date.isoformat(),
                        "owner_name": trip.owner_name,
                        "owner_email": trip.owner_email,
                        "status": trip.status
                    }
                },
                "status_code": 200
            }
        else:
            return {
                "body": {"error": "Trip not found"},
                "status_code": 404
            }
