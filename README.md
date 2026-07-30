# Valve Inventory API

A small REST API for managing hydraulic valve inventory records, built with FastAPI.

## Endpoints
- GET /valves — list all valves (optional type filter)
- GET /valves/{id} — get one valve
- POST /valves — create a valve
- PATCH /valves/{id} — update a valve
- DELETE /valves/{id} — delete a valve

## Setup
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. uvicorn src.main:app --reload
5. Visit http://127.0.0.1:8000/docs