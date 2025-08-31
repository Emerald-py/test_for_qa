import pytest
from ..api_methods.favorites_api import FavoritesAPI
from .data_generator import generate_data_with_color, generate_data_without_color


def test_create_place_with_mandatory_parameters(token):
    payload = generate_data_without_color()
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["title"] == payload["title"]
    assert resp_json["lat"] == payload["lat"]
    assert resp_json["lon"] == payload["lon"]
    assert resp_json["color"] is None


@pytest.mark.parametrize("color", ["BLUE", "GREEN", "RED", "YELLOW"])
def test_create_place_with_color(token, color):
    payload = generate_data_without_color()
    payload["color"] = color
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["title"] == payload["title"]
    assert resp_json["lat"] == payload["lat"]
    assert resp_json["lon"] == payload["lon"]
    assert resp_json["color"] == payload["color"]


def test_create_place_with_title_in_cyrillic(token):
    payload = generate_data_without_color()
    payload["title"] = "Кириллица"
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["title"] == payload["title"]
    assert resp_json["lat"] == payload["lat"]
    assert resp_json["lon"] == payload["lon"]
    assert resp_json["color"] is None


def test_create_place_with_title_with_numbers_and_punctuation_marks(token):
    payload = generate_data_without_color()
    payload["title"] = "Address 1234567890.,?!...;-:()«»"
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["title"] == payload["title"]
    assert resp_json["lat"] == payload["lat"]
    assert resp_json["lon"] == payload["lon"]
    assert resp_json["color"] is None


@pytest.mark.parametrize("coordinates", [(50.00, 50.00), (50.00, -50.00), (-50.00, -50.00), (-50.00, 50.00)])
def test_create_place_with_valid_coordinates_in_different_symbol_combinations(token, coordinates):
    payload = generate_data_without_color()
    payload["lat"] = coordinates[0]
    payload["lon"] = coordinates[1]
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["title"] == payload["title"]
    assert resp_json["lat"] == payload["lat"]
    assert resp_json["lon"] == payload["lon"]
    assert resp_json["color"] is None


@pytest.mark.parametrize("coordinates", [(00.00, 00.00), (-90.00, -180.00), (90.00, 180.00)])
def test_create_place_with_extreme_coordinate_values(token, coordinates):
    payload = generate_data_without_color()
    payload["lat"] = coordinates[0]
    payload["lon"] = coordinates[1]
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["title"] == payload["title"]
    assert resp_json["lat"] == payload["lat"]
    assert resp_json["lon"] == payload["lon"]
    assert resp_json["color"] is None


@pytest.mark.parametrize("title", ["W", "W" * 999])
def test_create_place_with_title_with_extreme_length_values(token, title):
    payload = generate_data_without_color()
    payload["title"] = title
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["title"] == payload["title"]
    assert resp_json["lat"] == payload["lat"]
    assert resp_json["lon"] == payload["lon"]
    assert resp_json["color"] is None


def test_create_place_without_title_parameter(token):
    payload = generate_data_without_color()
    del payload["title"]
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'title' является обязательным"


def test_create_place_with_empty_title_parameter(token):
    payload = generate_data_without_color()
    payload["title"] = ""
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'title' не может быть пустым"


def test_create_place_with_exceeded_title_length(token):
    payload = generate_data_without_color()
    payload["title"] = "W" * 1000
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'title' должен содержать не более 999 символов"


def test_create_place_without_the_lat_parameter(token):
    payload = generate_data_without_color()
    del payload["lat"]
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lat' является обязательным"


def test_create_place_with_empty_lat_parameter(token):
    payload = generate_data_without_color()
    payload["lat"] = None
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lat' является обязательным"


def test_create_place_without_lon_parameter(token):
    payload = generate_data_without_color()
    del payload["lon"]
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lon' является обязательным"


def test_create_place_with_empty_lon_parameter(token):
    payload = generate_data_without_color()
    payload["lon"] = None
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lon' является обязательным"


def test_create_place_with_lat_parameter_greater_than_allowed_value(token):
    payload = generate_data_without_color()
    payload["lat"] = 90.000001
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lat' должен быть не более 90"


def test_create_place_with_lat_parameter_less_than_allowed_value(token):
    payload = generate_data_without_color()
    payload["lat"] = -90.000001
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lat' должен быть не менее -90"


def test_create_place_with_lon_parameter_greater_than_allowed_value(token):
    payload = generate_data_without_color()
    payload["lon"] = 180.000001
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lon' должен быть не более 180"


def test_create_place_with_lon_parameter_less_than_allowed_value(token):
    payload = generate_data_without_color()
    payload["lon"] = -180.000001
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == "Параметр 'lon' должен быть не менее -180"


def test_create_place_with_color_parameter_not_in_list_valid_values(token):
    payload = generate_data_with_color()
    payload["color"] = "BLACK"
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == ("Параметр 'color' может быть одним из следующих значений: "
                                             "BLUE, GREEN, RED, YELLOW")


def test_create_place_with_empty_color_parameter(token):
    payload = generate_data_with_color()
    payload["color"] = ""
    response = FavoritesAPI.create_favorite(token, payload)
    assert response.status_code == 400
    resp_json = response.json()
    assert resp_json["error"]["message"] == ("Параметр 'color' может быть одним из следующих значений: "
                                             "BLUE, GREEN, RED, YELLOW")
