# src/services/profesor_service.py

from sqlalchemy.orm import Session
from src.models.models import Profesor
from src.schemas import ProfesorCreate, ProfesorUpdate

# Layer: Service Layer
# This layer contains the business logic for the application.

class ProfesorService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_profesores(self):
        return self.db.query(Profesor).all()

    def get_profesor_by_id(self, profesor_id: int):
        return self.db.query(Profesor).filter(Profesor.profesor_id == profesor_id).first()

    def create_profesor(self, profesor: ProfesorCreate):
        new_profesor = Profesor(
            nombre=profesor.nombre,
            apellido=profesor.apellido,
            dni=profesor.dni,
            email=profesor.email,
            especialidad=profesor.especialidad,
            titulo_academico=profesor.titulo_academico,
            telefono=profesor.telefono
        )
        self.db.add(new_profesor)
        self.db.commit()
        self.db.refresh(new_profesor)
        return new_profesor

    def update_profesor(self, profesor_id: int, profesor_data: ProfesorUpdate):
        profesor = self.get_profesor_by_id(profesor_id)
        if profesor:
            for key, value in profesor_data.dict(exclude_unset=True).items():
                setattr(profesor, key, value)
            self.db.commit()
            self.db.refresh(profesor)
        return profesor

    def delete_profesor(self, profesor_id: int):
        profesor = self.get_profesor_by_id(profesor_id)
        if profesor:
            self.db.delete(profesor)
            self.db.commit()
        return profesor
