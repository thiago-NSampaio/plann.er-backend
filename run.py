from src.main.server.server import app
from src.models.settings.db_connection_handler import DBConnectionHandler
from src.models.settings.initDB import InitDB

if __name__ == "__main__":
    InitDB.create_tables()
    db_connection_handler = DBConnectionHandler()
    db_connection_handler.connect()
    db_connection_handler.get_connection()
    app.run(host="0.0.0.0", port=3555, debug=True)
