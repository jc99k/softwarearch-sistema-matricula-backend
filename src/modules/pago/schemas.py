# src/modules/pago/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class PagoBase(BaseModel):
    matricula_id: int
    monto: float
    metodo_pago: str
    referencia: Optional[str] = None

class PagoCreate(PagoBase):
    pass

class PagoUpdate(PagoBase):
    matricula_id: Optional[int] = None
    monto: Optional[float] = None
    metodo_pago: Optional[str] = None

class Pago(PagoBase):
    pago_id: int
    fecha_pago: date
    estado: str

    class Config:
        orm_mode = True
