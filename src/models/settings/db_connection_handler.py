from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'sqlite:///storage.db'
        self.__engine = create_engine(self.__connection_string)
        self.__session = None

    def connect(self):
        self.__session = sessionmaker(bind=self.__engine)()
        return self.__session

    def get_connection(self):
        if self.__session is None:
            self.connect()
        return self.__session

    def close_connection(self):
        if self.__session:
            self.__session.close()
            self.__session = None
