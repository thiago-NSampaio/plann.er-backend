from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def registry_participant(self,participant_infos:dict):
        cursor = self.__conn.cursor()
        cursor.execute(
        '''INSERT INTO participants(id, trip_id, emails_to_invite_id, name)
        VALUES(?, ?, ?, ?)''',(
            participant_infos["id"],
            participant_infos["trip_id"],
            participant_infos["emails_to_invite_id"],
            participant_infos["name"],
            )
        )

        self.__conn.commit()

    def find_participants_from_trip(self, tripId) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT p.id, p.name, p.is_confirmed, e.email
               FROM participants as p
               JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
               WHERE p.trip_id = ?
               ''',(tripId,)
        )
        participants = cursor.fetchall()
        return participants
    
    def update_participant_status(self, participant_id: str) ->None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''UPDATE participants
            SET is_confirmed = 1
            WHERE id= ?''',(participant_id,)
        )
        self.__conn.commit()

    def delete_participant(self, participant_id:str, trip_Id: str)-> None:
        cursor = self.__conn.cursor()
        cursor.execute('DELETE FROM participants WHERE id = ? and trip_id = ?', (participant_id,trip_Id))
        self.__conn.commit()


