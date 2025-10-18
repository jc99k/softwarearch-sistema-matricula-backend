# src/modules/estudiante/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    email: str
    telefono: Optional[str] = None
    fecha_nacimiento: date
    direccion: Optional[str] = None

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(EstudianteBase):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    dni: Optional[str] = None
    email: Optional[str] = None
    fecha_nacimiento: Optional[date] = None

class Estudiante(EstudianteBase):
    estudiante_id: int
    activo: bool

    class Config:
        orm_mode = True
