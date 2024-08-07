from src.main.server.server import app
from src.models.settings.db_connection_handler import DBConnectionHandler
from src.models.settings.initDB import InitDB


def start_app():
    InitDB.create_tables()
    db_connection_handler = DBConnectionHandler()
    db_connection_handler.connect()


start_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333, debug=False)
