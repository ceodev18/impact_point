# Pokémon Scouting App

A backend Flask application to import, store, and retrieve Pokémon data from the PokéAPI.

---

## Setup

```bash
git clone <this-repo>
cd pokemon-scouting-app
docker-compose up --build
```

---

## Usage

### 🔹 Import Pokémon

Make a `POST` request to `/api/import` with a JSON payload:

```json
{
  "names": ["pikachu", "charizard"]
}
```

### 🔹 List Stored Pokémon

Make a `GET` request to `/api/pokemons`:

```bash
curl http://localhost:5000/pokemons
```

This returns all stored Pokémon in JSON format.

---

## Adding More Pokémon

You can either:

- Edit the default list in `utils.py`
- Or pass names directly in the JSON payload when calling `/api/import`

---

## Running Tests

```bash
docker-compose run pokemon-app pytest
```

---

## Configuration

Main configuration is located in `config.py`:

```python
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"
MAX_WORKERS = 5
```

- You can increase `MAX_WORKERS` to improve parallel fetch performance.

---

## API Documentation (Swagger)

Interactive Swagger UI is available at:

[http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

## Project Structure

```
pokemon-scouting-app/
├── app/
│   ├── __init__.py       # Flask + Swagger setup
│   ├── models.py         # SQLAlchemy model
│   ├── routes.py         # API routes
│   ├── services.py       # Fetch + sanitize + store logic
│   └── utils.py          # Default Pokémon list
├── tests/
│   └── test_services.py  # Unit tests
├── config.py             # Global configuration
├── Dockerfile            # App container
├── docker-compose.yml    # Docker orchestration
└── README.md             # Project documentation
```

---
