import os
import pytest
from pygita import Client

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


@pytest.fixture(scope="session")
def client():
    return Client(CLIENT_ID, CLIENT_SECRET)


# @pytest.fixture(scope="session")
# def verse(client):
#     return client.get_verse(4,5)


# @pytest.fixture(scope="session")
# def chapter(client):
#     return client.get_chapter(4)
