# src/services/pago_service.py

from sqlalchemy.orm import Session
from .models import Pago
from .schemas import PagoCreate, PagoUpdate

# Layer: Service Layer
# This layer contains the business logic for the application.

class PagoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_pagos(self):
        return self.db.query(Pago).all()

    def get_pago_by_id(self, pago_id: int):
        return self.db.query(Pago).filter(Pago.pago_id == pago_id).first()

    def create_pago(self, pago: PagoCreate):
        new_pago = Pago(
            matricula_id=pago.matricula_id,
            monto=pago.monto,
            metodo_pago=pago.metodo_pago,
            referencia=pago.referencia
        )
        self.db.add(new_pago)
        self.db.commit()
        self.db.refresh(new_pago)
        return new_pago

    def update_pago(self, pago_id: int, pago_data: PagoUpdate):
        pago = self.get_pago_by_id(pago_id)
        if pago:
            for key, value in pago_data.dict(exclude_unset=True).items():
                setattr(pago, key, value)
            self.db.commit()
            self.db.refresh(pago)
        return pago

    def delete_pago(self, pago_id: int):
        pago = self.get_pago_by_id(pago_id)
        if pago:
            self.db.delete(pago)
            self.db.commit()
        return pago
