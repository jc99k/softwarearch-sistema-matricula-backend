# src/modules/facultad/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class FacultadBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None
    decano: Optional[str] = None

class FacultadCreate(FacultadBase):
    pass

class FacultadUpdate(FacultadBase):
    nombre: Optional[str] = None

class Facultad(FacultadBase):
    facultad_id: int
    activo: bool

    class Config:
        orm_mode = True
