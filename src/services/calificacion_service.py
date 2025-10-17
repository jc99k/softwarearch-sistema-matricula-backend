# src/services/calificacion_service.py

from sqlalchemy.orm import Session
from src.models.models import Calificacion
from src.schemas import CalificacionCreate

# Layer: Service Layer
# This layer contains the business logic for the application.

class CalificacionService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_calificaciones(self):
        return self.db.query(Calificacion).all()

    def get_calificacion_by_id(self, calificacion_id: int):
        return self.db.query(Calificacion).filter(Calificacion.calificacion_id == calificacion_id).first()

    def create_calificacion(self, calificacion: CalificacionCreate):
        new_calificacion = Calificacion(
            matricula_id=calificacion.matricula_id,
            nota=calificacion.nota,
            observacion=calificacion.observacion
        )
        self.db.add(new_calificacion)
        self.db.commit()
        self.db.refresh(new_calificacion)
        return new_calificacion