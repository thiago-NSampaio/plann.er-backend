from src.main.server.server import app
from src.models.settings.db_connection_handler import db_connection_handler

if __name__ == "__main__":
    db_connection_handler.connect()
    db_connection_handler.get_connection()
    app.run(host="0.0.0.0", port=3555, debug=True)