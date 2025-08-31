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































