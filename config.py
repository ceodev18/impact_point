import os

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"
MAX_WORKERS = 5

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'scouting.db')

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_WORKERS = MAX_WORKERS
    POKEAPI_BASE_URL = POKEAPI_BASE_URL
