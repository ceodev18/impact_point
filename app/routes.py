from flask import Blueprint, jsonify, request
from .services import import_pokemons, get_all_pokemons
from flasgger import swag_from

bp = Blueprint("api", __name__)

@bp.route("/api/import", methods=["POST"])
@swag_from({
    'tags': ['Pokémon'],
    'description': 'Import Pokémon data by names',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': {
                'type': 'object',
                'properties': {
                    'names': {
                        'type': 'array',
                        'items': {'type': 'string'}
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Pokémon imported successfully'
        }
    }
})
def import_pokemon():
    names = request.json.get("names") if request.is_json else None
    return jsonify(import_pokemons(names))

@bp.route("/api/pokemons", methods=["GET"])
@swag_from({
    'tags': ['Pokémon'],
    'description': 'List all stored Pokémon',
    'responses': {
        '200': {
            'description': 'List of Pokémon',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'base_experience': {'type': 'integer'},
                        'height': {'type': 'integer'},
                        'weight': {'type': 'integer'},
                        'types': {'type': 'string'},
                        'stats': {'type': 'object'},
                        'abilities': {'type': 'string'},
                        'sprite_url': {'type': 'string'},
                        'cry_url': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def get_pokemons():
    return jsonify(get_all_pokemons())
