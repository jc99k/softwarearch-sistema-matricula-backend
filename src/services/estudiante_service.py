# src/services/estudiante_service.py

from src.models.models import Estudiante
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class EstudianteService:

    def get_all_estudiantes(self):
        return Estudiante.query.all()

    def get_estudiante_by_id(self, estudiante_id):
        return Estudiante.query.get(estudiante_id)

    def create_estudiante(self, data):
        new_estudiante = Estudiante(
            nombre=data['nombre'],
            apellido=data['apellido'],
            dni=data['dni'],
            email=data['email'],
            fecha_nacimiento=data['fecha_nacimiento'],
            direccion=data.get('direccion'),
            telefono=data.get('telefono')
        )
        db.session.add(new_estudiante)
        db.session.commit()
        return new_estudiante
