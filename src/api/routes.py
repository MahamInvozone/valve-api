from fastapi import APIRouter, HTTPException
from typing import Optional
from src.models import Valve, ValveUpdate
from src import services

router = APIRouter()


@router.get("/valves")
def list_valves(valve_type: Optional[str] = None):
    return services.get_all_valves(valve_type)


@router.get("/valves/{valve_id}")
def get_valve(valve_id: int):
    valve = services.get_valve_by_id(valve_id)
    if valve is None:
        raise HTTPException(status_code=404, detail="Valve not found")
    return valve


@router.post("/valves", status_code=201)
def create_valve(valve: Valve):
    return services.create_valve(valve)


@router.patch("/valves/{valve_id}")
def update_valve(valve_id: int, updates: ValveUpdate):
    valve = services.update_valve(valve_id, updates)
    if valve is None:
        raise HTTPException(status_code=404, detail="Valve not found")
    return valve


@router.delete("/valves/{valve_id}", status_code=204)
def delete_valve(valve_id: int):
    success = services.delete_valve(valve_id)
    if not success:
        raise HTTPException(status_code=404, detail="Valve not found")