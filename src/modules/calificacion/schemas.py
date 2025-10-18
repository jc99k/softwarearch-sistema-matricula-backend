# src/modules/calificacion/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class CalificacionBase(BaseModel):
    matricula_id: int
    nota: float
    observacion: Optional[str] = None

class CalificacionCreate(CalificacionBase):
    pass

class CalificacionUpdate(CalificacionBase):
    matricula_id: Optional[int] = None
    nota: Optional[float] = None

class Calificacion(CalificacionBase):
    calificacion_id: int

    class Config:
        orm_mode = True
