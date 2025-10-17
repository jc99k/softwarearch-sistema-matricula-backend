# src/services/curso_service.py

from sqlalchemy.orm import Session
from src.models.models import Curso
from src.schemas import CursoCreate, CursoUpdate

# Layer: Service Layer
# This layer contains the business logic for the application.

class CursoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_cursos(self):
        return self.db.query(Curso).all()

    def get_curso_by_id(self, curso_id: int):
        return self.db.query(Curso).filter(Curso.curso_id == curso_id).first()

    def create_curso(self, curso: CursoCreate):
        new_curso = Curso(
            carrera_id=curso.carrera_id,
            codigo=curso.codigo,
            nombre=curso.nombre,
            descripcion=curso.descripcion,
            creditos=curso.creditos,
            nivel_semestre=curso.nivel_semestre
        )
        self.db.add(new_curso)
        self.db.commit()
        self.db.refresh(new_curso)
        return new_curso

    def update_curso(self, curso_id: int, curso_data: CursoUpdate):
        curso = self.get_curso_by_id(curso_id)
        if curso:
            for key, value in curso_data.dict(exclude_unset=True).items():
                setattr(curso, key, value)
            self.db.commit()
            self.db.refresh(curso)
        return curso

    def delete_curso(self, curso_id: int):
        curso = self.get_curso_by_id(curso_id)
        if curso:
            self.db.delete(curso)
            self.db.commit()
        return curso
