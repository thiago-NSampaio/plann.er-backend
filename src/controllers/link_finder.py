class LinkFinder:
    def __init__(self, link_repository) -> None:
        if link_repository is None:
            raise ValueError("link_repository cannot be None")
        self.__link_repository = link_repository

    def finder(self, trip_id):

        try:
            links = self.__link_repository.find_links_from_trip(trip_id)
            if links:
                links_info = [{
                    "id": link.id,
                    "url": link.link,
                    "trip_id": link.trip_id,
                    "title": link.title,
                } for link in links]
            else:
                links_info = []
            return {
                "body": {"links": links_info},
                "status_code": 200
            }

        except Exception as exception:
            return {
                "body": {"error": "Internal Server Error", "message": str(exception)},
                "status_code": 500
            }
