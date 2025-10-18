# src/services/facultad_service.py

from sqlalchemy.orm import Session
from .models import Facultad
from .schemas import FacultadCreate, FacultadUpdate

# Layer: Service Layer
# This layer contains the business logic for the application.

class FacultadService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_facultades(self):
        return self.db.query(Facultad).all()

    def get_facultad_by_id(self, facultad_id: int):
        return self.db.query(Facultad).filter(Facultad.facultad_id == facultad_id).first()

    def create_facultad(self, facultad: FacultadCreate):
        new_facultad = Facultad(
            nombre=facultad.nombre,
            descripcion=facultad.descripcion,
            ubicacion=facultad.ubicacion,
            decano=facultad.decano
        )
        self.db.add(new_facultad)
        self.db.commit()
        self.db.refresh(new_facultad)
        return new_facultad

    def update_facultad(self, facultad_id: int, facultad_data: FacultadUpdate):
        facultad = self.get_facultad_by_id(facultad_id)
        if facultad:
            for key, value in facultad_data.dict(exclude_unset=True).items():
                setattr(facultad, key, value)
            self.db.commit()
            self.db.refresh(facultad)
        return facultad

    def delete_facultad(self, facultad_id: int):
        facultad = self.get_facultad_by_id(facultad_id)
        if facultad:
            self.db.delete(facultad)
            self.db.commit()
        return facultad
