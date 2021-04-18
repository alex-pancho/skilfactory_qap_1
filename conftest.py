import calc
import pytest
import apihelper


@pytest.fixture
def authenticate(testuser):
    apihelper.login(testuser)

@pytest.fixture
def testuser():
    return apihelper.user