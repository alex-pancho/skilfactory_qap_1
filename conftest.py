import calc
import pytest
import apihelper
import tools


@pytest.fixture
def authenticate(testuser):
    apihelper.login(testuser)


@pytest.fixture
def signin(testuser):
    tools.login(testuser)

@pytest.fixture
def testuser():
    return apihelper.user