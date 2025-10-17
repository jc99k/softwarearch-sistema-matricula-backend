# src/services/calificacion_service.py

from src.models.models import Calificacion
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class CalificacionService:

    def get_all_calificaciones(self):
        return Calificacion.query.all()

    def get_calificacion_by_id(self, calificacion_id):
        return Calificacion.query.get(calificacion_id)

    def create_calificacion(self, data):
        new_calificacion = Calificacion(
            matricula_id=data['matricula_id'],
            nota=data['nota'],
            observacion=data.get('observacion')
        )
        db.session.add(new_calificacion)
        db.session.commit()
        return new_calificacion
