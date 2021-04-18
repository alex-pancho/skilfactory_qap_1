import apihelper
import pytest


def test_get_key_positive():
    user = apihelper.user
    result = apihelper.get_apikey(user["email"], user["password"])
    print(result.get("key"))
    assert result.get("key") is not None