import random
import string


def generate_title() -> str:
    return "Fav_" + "".join(random.choices(string.ascii_letters, k=5))


def generate_lat() -> float:
    return round(random.uniform(-90.00, 90.00), 6)


def generate_lon() -> float:
    return round(random.uniform(-180.00, 180.00), 6)


def generate_color() -> str:
    colors = ["BLUE", "GREEN", "RED", "YELLOW"]
    return random.choice(colors)


def generate_data_with_color() -> dict:
    return {
        "title": generate_title(),
        "lat": generate_lat(),
        "lon": generate_lon(),
        "color": generate_color(),
    }


def generate_data_without_color() -> dict:
    return {
        "title": generate_title(),
        "lat": generate_lat(),
        "lon": generate_lon()
    }
