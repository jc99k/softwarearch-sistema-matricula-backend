# src/services/facultad_service.py

from sqlalchemy.orm import Session
from src.models.models import Facultad
from src.schemas import FacultadCreate

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