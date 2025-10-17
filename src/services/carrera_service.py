# src/services/carrera_service.py

from sqlalchemy.orm import Session
from src.models.models import Carrera
from src.schemas import CarreraCreate

# Layer: Service Layer
# This layer contains the business logic for the application.

class CarreraService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_carreras(self):
        return self.db.query(Carrera).all()

    def get_carrera_by_id(self, carrera_id: int):
        return self.db.query(Carrera).filter(Carrera.carrera_id == carrera_id).first()

    def create_carrera(self, carrera: CarreraCreate):
        new_carrera = Carrera(
            facultad_id=carrera.facultad_id,
            nombre=carrera.nombre,
            descripcion=carrera.descripcion,
            duracion_semestres=carrera.duracion_semestres,
            titulo_otorgado=carrera.titulo_otorgado
        )
        self.db.add(new_carrera)
        self.db.commit()
        self.db.refresh(new_carrera)
        return new_carrera