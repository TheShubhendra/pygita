import os
import pytest

CLIENT_ID = os.get_environ("CLIENT_ID")
CLIENT_SECRET = os.get_environ("CLIENT_SECRET")


@pytest.fixture(scope="session", autouse=True)
def generate_token(CLIENT_ID, CLIENT_SECRET):
    