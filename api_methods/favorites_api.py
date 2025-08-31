import requests
from ..endpoints import Endpoints


class FavoritesAPI:
    @staticmethod
    def create_favorite(token: str, data: dict):
        url = f"{Endpoints.BASE_URL}{Endpoints.FAVORITES_ENDPOINT}"
        cookies = {"token": token}
        response = requests.post(url, data=data, cookies=cookies)
        return response
