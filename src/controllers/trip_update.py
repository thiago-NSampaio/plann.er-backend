class TripUpdate:
    def __init__(self,trips_repository) -> None:
        self.__trips_repository = trips_repository

    def update(self,tripId,body)-> dict:
        try:
            trips_update_info ={
                "destination": body["destination"],
                "start_date": body["start_date"],
                "end_date": body["end_date"]
            }
            self.__trips_repository.upadate_trip(tripId,trips_update_info)

            return{
                "body":None,"status_code":204
            }
        except Exception as e:
            return {
                "body":{"error":"Bad Request", "message": str(e)},
                "status_code":400
            }