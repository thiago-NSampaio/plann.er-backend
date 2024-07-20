from sqlite3 import Connection

class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def registry_activities(self,activities_infos:dict):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''INSERT INTO activities(id, trip_id, title, occurs_at)
            VALUES(?, ?, ?, ?),
            ''',(
                activities_infos["id"],
                activities_infos["trip_id"],
                activities_infos["title"],
                activities_infos["occurs_at"],
            )
        )
        self.__conn.commit()

    def find_activities_from_trip(self, tripId) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM activities
               WHERE a.trip_id = ?
               ''',(tripId,)
        )
        activities = cursor.fetchall()
        return activities
    
