# src/services/estudiante_service.py

from sqlalchemy.orm import Session
from src.models.models import Estudiante
from src.schemas import EstudianteCreate

# Layer: Service Layer
# This layer contains the business logic for the application.

class EstudianteService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_estudiantes(self):
        return self.db.query(Estudiante).all()

    def get_estudiante_by_id(self, estudiante_id: int):
        return self.db.query(Estudiante).filter(Estudiante.estudiante_id == estudiante_id).first()

    def create_estudiante(self, estudiante: EstudianteCreate):
        new_estudiante = Estudiante(
            nombre=estudiante.nombre,
            apellido=estudiante.apellido,
            dni=estudiante.dni,
            email=estudiante.email,
            fecha_nacimiento=estudiante.fecha_nacimiento,
            direccion=estudiante.direccion,
            telefono=estudiante.telefono
        )
        self.db.add(new_estudiante)
        self.db.commit()
        self.db.refresh(new_estudiante)
        return new_estudiante