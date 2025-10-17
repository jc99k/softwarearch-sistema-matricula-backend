# src/services/seccion_service.py

from src.models.models import Seccion
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class SeccionService:

    def get_all_secciones(self):
        return Seccion.query.all()

    def get_seccion_by_id(self, seccion_id):
        return Seccion.query.get(seccion_id)

    def create_seccion(self, data):
        new_seccion = Seccion(
            curso_id=data['curso_id'],
            profesor_id=data['profesor_id'],
            codigo=data['codigo'],
            capacidad_maxima=data['capacidad_maxima'],
            aula=data.get('aula'),
            horario=data.get('horario'),
            dias=data.get('dias'),
            periodo_academico=data['periodo_academico'],
            fecha_inicio=data.get('fecha_inicio'),
            fecha_fin=data.get('fecha_fin')
        )
        db.session.add(new_seccion)
        db.session.commit()
        return new_seccion
