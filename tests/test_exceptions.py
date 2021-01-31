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
