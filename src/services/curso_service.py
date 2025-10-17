# src/services/curso_service.py

from src.models.models import Curso
from src.db import db

# Layer: Service Layer
# This layer contains the business logic for the application.

class CursoService:

    def get_all_cursos(self):
        return Curso.query.all()

    def get_curso_by_id(self, curso_id):
        return Curso.query.get(curso_id)

    def create_curso(self, data):
        new_curso = Curso(
            carrera_id=data['carrera_id'],
            codigo=data['codigo'],
            nombre=data['nombre'],
            descripcion=data.get('descripcion'),
            creditos=data['creditos'],
            nivel_semestre=data['nivel_semestre']
        )
        db.session.add(new_curso)
        db.session.commit()
        return new_curso
