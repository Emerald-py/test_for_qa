import pytest
from ..api_methods.auth_api import AuthAPI


@pytest.fixture
def token():
    return AuthAPI.get_token()
