# src/modules/profesor/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class ProfesorBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    email: str
    telefono: Optional[str] = None
    especialidad: Optional[str] = None
    titulo_academico: Optional[str] = None

class ProfesorCreate(ProfesorBase):
    pass

class ProfesorUpdate(ProfesorBase):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    dni: Optional[str] = None
    email: Optional[str] = None

class Profesor(ProfesorBase):
    profesor_id: int
    activo: bool

    class Config:
        orm_mode = True
