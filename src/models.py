from pydantic import BaseModel
from typing import Optional


class Valve(BaseModel):
    id: int
    model: str
    valve_type: str
    max_pressure_bar: float
    manufacturer: str
    price: float
    in_stock: bool


class ValveUpdate(BaseModel):
    model: Optional[str] = None
    valve_type: Optional[str] = None
    max_pressure_bar: Optional[float] = None
    manufacturer: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None