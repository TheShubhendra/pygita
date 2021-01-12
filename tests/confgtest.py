import os
import pytest
from pygita import Client

CLIENT_ID = os.get_environ("CLIENT_ID")
CLIENT_SECRET = os.get_environ("CLIENT_SECRET")


@pytest.fixture(scope="session", autouse=True)
def create_client(CLIENT_ID, CLIENT_SECRET):
    return Client(CLIENT_ID, CLIENT_SECRET)
