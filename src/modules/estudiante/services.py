# src/services/estudiante_service.py

from sqlalchemy.orm import Session
from .models import Estudiante
from .schemas import EstudianteCreate, EstudianteUpdate

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

    def update_estudiante(self, estudiante_id: int, estudiante_data: EstudianteUpdate):
        estudiante = self.get_estudiante_by_id(estudiante_id)
        if estudiante:
            for key, value in estudiante_data.dict(exclude_unset=True).items():
                setattr(estudiante, key, value)
            self.db.commit()
            self.db.refresh(estudiante)
        return estudiante

    def delete_estudiante(self, estudiante_id: int):
        estudiante = self.get_estudiante_by_id(estudiante_id)
        if estudiante:
            self.db.delete(estudiante)
            self.db.commit()
        return estudiante
