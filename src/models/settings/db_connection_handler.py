import sqlite3
from sqlite3 import Connection

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        self.__conn = sqlite3.connect(self.__connection_string, check_same_thread=False)

    def get_connection(self) -> Connection:
        if self.__conn is None:
            raise ConnectionError("Database connection is not established.")
        return self.__conn

    def disconnect(self) -> None:
        if self.__conn:
            self.__conn.close()
            self.__conn = None

db_connection_handler = DbConnectionHandler()
