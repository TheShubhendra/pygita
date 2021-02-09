import pytest
from pygita import Client
from pygita.exceptions import (
    AuthorizationError,
)


def test_wrong_crendetials():
    client = Client("ABCD", "EFGH")
    with pytest.raises(AuthorizationError) as e:
        assert client.get_verse(1, 1)
    assert str(e.value) == "Unable to get access_token."


def test_base_exception(client):
    with pytest.raises(Exception):
        assert client.get_verse(900, 800)
