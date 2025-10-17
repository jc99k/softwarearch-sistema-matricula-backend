# src/services/matricula_service.py

from src.models.models import Matricula
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class MatriculaService:

    def get_all_matriculas(self):
        return Matricula.query.all()

    def get_matricula_by_id(self, matricula_id):
        return Matricula.query.get(matricula_id)

    def create_matricula(self, data):
        new_matricula = Matricula(
            estudiante_id=data['estudiante_id'],
            seccion_id=data['seccion_id'],
            costo=data['costo'],
            metodo_pago=data.get('metodo_pago')
        )
        db.session.add(new_matricula)
        db.session.commit()
        return new_matricula
