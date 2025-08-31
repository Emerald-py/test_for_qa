import requests
from ..endpoints import Endpoints


class AuthAPI:
    @staticmethod
    def get_token():
        url = f"{Endpoints.BASE_URL}{Endpoints.AUTH_ENDPOINT}"
        response = requests.post(url)
        response.raise_for_status()
        token = response.cookies.get("token")
        return token
