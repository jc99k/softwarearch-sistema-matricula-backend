# src/modules/curso/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class CursoBase(BaseModel):
    carrera_id: int
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    creditos: int
    nivel_semestre: int

class CursoCreate(CursoBase):
    pass

class CursoUpdate(CursoBase):
    carrera_id: Optional[int] = None
    codigo: Optional[str] = None
    nombre: Optional[str] = None

class Curso(CursoBase):
    curso_id: int
    activo: bool

    class Config:
        orm_mode = True
