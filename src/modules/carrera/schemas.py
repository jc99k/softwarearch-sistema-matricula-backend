# src/modules/carrera/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class CarreraBase(BaseModel):
    facultad_id: int
    nombre: str
    descripcion: Optional[str] = None
    duracion_semestres: int
    titulo_otorgado: Optional[str] = None

class CarreraCreate(CarreraBase):
    pass

class CarreraUpdate(CarreraBase):
    facultad_id: Optional[int] = None
    nombre: Optional[str] = None

class Carrera(CarreraBase):
    carrera_id: int
    activo: bool

    class Config:
        orm_mode = True
