# src/services/pago_service.py

from src.models.models import Pago
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class PagoService:

    def get_all_pagos(self):
        return Pago.query.all()

    def get_pago_by_id(self, pago_id):
        return Pago.query.get(pago_id)

    def create_pago(self, data):
        new_pago = Pago(
            matricula_id=data['matricula_id'],
            monto=data['monto'],
            metodo_pago=data['metodo_pago'],
            referencia=data.get('referencia')
        )
        db.session.add(new_pago)
        db.session.commit()
        return new_pago
