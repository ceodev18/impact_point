import requests
from .models import Pokemon
from . import db
import json
from .utils import get_default_pokemon_list
from flask import current_app
from concurrent.futures import ThreadPoolExecutor

def fetch_pokemon_data(name: str, base_url: str):
    response = requests.get(f"{base_url}/pokemon/{name.lower()}")
    if response.status_code != 200:
        raise ValueError(f"Pokemon '{name}' not found.")
    return response.json()

def sanitize_pokemon_data(data):
    return {
        "name": data["name"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "weight": data["weight"],
        "types": ", ".join(t["type"]["name"] for t in data["types"]),
        "stats": json.dumps({s["stat"]["name"]: s["base_stat"] for s in data["stats"]}),
        "abilities": ", ".join(a["ability"]["name"] for a in data["abilities"]),
        "sprite_url": data["sprites"]["front_default"],
        "cry_url": data.get("cries", {}).get("latest")
    }

def store_pokemon(data):
    if Pokemon.query.filter_by(name=data["name"]).first():
        return
    pokemon = Pokemon(**data)
    db.session.add(pokemon)
    db.session.commit()

def import_pokemons(names=None):
    names = names or get_default_pokemon_list()
    fetched_results = []

    # get config out of thread
    base_url = current_app.config.get("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2")
    max_workers = current_app.config.get("MAX_WORKERS", 5)

    def fetch_and_clean(name):
        try:
            raw = fetch_pokemon_data(name, base_url)
            clean = sanitize_pokemon_data(raw)
            return {"name": name, "data": clean, "error": None}
        except Exception as e:
            return {"name": name, "data": None, "error": str(e)}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        fetched_results = list(executor.map(fetch_and_clean, names))

    result = []
    for item in fetched_results:
        if item["error"]:
            result.append({"name": item["name"], "status": "error", "message": item["error"]})
        else:
            try:
                store_pokemon(item["data"])
                result.append({"name": item["name"], "status": "success"})
            except Exception as e:
                result.append({"name": item["name"], "status": "error", "message": str(e)})

    return result

def get_all_pokemons():
    pokemons = Pokemon.query.all()
    result = []
    for p in pokemons:
        result.append({
            "id": p.id,
            "name": p.name,
            "base_experience": p.base_experience,
            "height": p.height,
            "weight": p.weight,
            "types": p.types,
            "stats": json.loads(p.stats),
            "abilities": p.abilities,
            "sprite_url": p.sprite_url,
            "cry_url": p.cry_url
        })
    return result
