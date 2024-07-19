import pytest
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler
import uuid

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())


# pytest.mark(reason="Interação com o Banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_info = {
        "id": link_id,
        "link": 'reserva@res.com',
        "trip_id": trip_id,
        "title":"Hotel"
    }

    links_repository.registry_link(links_info)

# pytest.mark(reason="Interação com o Banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links = links_repository.find_links_from_trip(trip_id)
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)

    print(links)

