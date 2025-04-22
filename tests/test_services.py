# tests/test_services.py
import pytest
from app.services import fetch_pokemon_data, sanitize_pokemon_data
from app import create_app

@pytest.fixture(scope="module")
def app_context():
    app = create_app()
    with app.app_context():
        yield app

@pytest.mark.parametrize("name", ["pikachu", "charizard"])
def test_fetch_pokemon_data(app_context, name):
    base_url = app_context.config["POKEAPI_BASE_URL"]
    data = fetch_pokemon_data(name, base_url)
    assert data["name"] == name.lower()

def test_sanitize_pokemon_data(app_context):
    base_url = app_context.config["POKEAPI_BASE_URL"]
    raw = fetch_pokemon_data("pikachu", base_url)
    clean = sanitize_pokemon_data(raw)
    assert clean["name"] == "pikachu"
    assert "speed" in clean["stats"]
