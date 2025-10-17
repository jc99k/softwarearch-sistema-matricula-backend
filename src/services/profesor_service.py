# src/services/profesor_service.py

from src.models.models import Profesor
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class ProfesorService:

    def get_all_profesores(self):
        return Profesor.query.all()

    def get_profesor_by_id(self, profesor_id):
        return Profesor.query.get(profesor_id)

    def create_profesor(self, data):
        new_profesor = Profesor(
            nombre=data['nombre'],
            apellido=data['apellido'],
            dni=data['dni'],
            email=data['email'],
            especialidad=data.get('especialidad'),
            titulo_academico=data.get('titulo_academico'),
            telefono=data.get('telefono')
        )
        db.session.add(new_profesor)
        db.session.commit()
        return new_profesor
