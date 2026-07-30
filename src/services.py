from typing import Optional
from src.models import Valve, ValveUpdate

# In-memory "database" — just a Python list for now
valves: list[Valve] = []


def get_all_valves(valve_type: Optional[str] = None) -> list[Valve]:
    if valve_type:
        return [v for v in valves if v.valve_type == valve_type]
    return valves


def get_valve_by_id(valve_id: int) -> Optional[Valve]:
    for v in valves:
        if v.id == valve_id:
            return v
    return None


def create_valve(valve: Valve) -> Valve:
    valves.append(valve)
    return valve


def update_valve(valve_id: int, updates: ValveUpdate) -> Optional[Valve]:
    valve = get_valve_by_id(valve_id)
    if valve is None:
        return None

    update_data = updates.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(valve, field, value)

    return valve


def delete_valve(valve_id: int) -> bool:
    valve = get_valve_by_id(valve_id)
    if valve is None:
        return False
    valves.remove(valve)
    return True