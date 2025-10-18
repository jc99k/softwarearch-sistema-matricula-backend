# src/modules/matricula/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class MatriculaBase(BaseModel):
    estudiante_id: int
    seccion_id: int
    costo: float
    metodo_pago: Optional[str] = None

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaUpdate(MatriculaBase):
    estudiante_id: Optional[int] = None
    seccion_id: Optional[int] = None
    costo: Optional[float] = None

class Matricula(MatriculaBase):
    matricula_id: int
    fecha_matricula: date
    estado: str

    class Config:
        orm_mode = True
