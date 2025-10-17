# src/services/carrera_service.py

from src.models.models import Carrera
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class CarreraService:

    def get_all_carreras(self):
        return Carrera.query.all()

    def get_carrera_by_id(self, carrera_id):
        return Carrera.query.get(carrera_id)

    def create_carrera(self, data):
        new_carrera = Carrera(
            facultad_id=data['facultad_id'],
            nombre=data['nombre'],
            descripcion=data.get('descripcion'),
            duracion_semestres=data['duracion_semestres'],
            titulo_otorgado=data.get('titulo_otorgado')
        )
        db.session.add(new_carrera)
        db.session.commit()
        return new_carrera
