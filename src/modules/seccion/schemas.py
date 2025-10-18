# src/modules/seccion/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class SeccionBase(BaseModel):
    curso_id: int
    profesor_id: int
    codigo: str
    capacidad_maxima: int
    aula: Optional[str] = None
    horario: Optional[str] = None
    dias: Optional[str] = None
    periodo_academico: str
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None

class SeccionCreate(SeccionBase):
    pass

class SeccionUpdate(SeccionBase):
    curso_id: Optional[int] = None
    profesor_id: Optional[int] = None
    codigo: Optional[str] = None

class Seccion(SeccionBase):
    seccion_id: int
    activo: bool

    class Config:
        orm_mode = True
