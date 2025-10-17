# src/services/facultad_service.py

from src.models.models import Facultad
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class FacultadService:

    def get_all_facultades(self):
        return Facultad.query.all()

    def get_facultad_by_id(self, facultad_id):
        return Facultad.query.get(facultad_id)

    def create_facultad(self, data):
        new_facultad = Facultad(
            nombre=data['nombre'],
            descripcion=data.get('descripcion'),
            ubicacion=data.get('ubicacion'),
            decano=data.get('decano')
        )
        db.session.add(new_facultad)
        db.session.commit()
        return new_facultad
