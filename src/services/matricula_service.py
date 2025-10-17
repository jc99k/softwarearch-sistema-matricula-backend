# src/services/matricula_service.py

from sqlalchemy.orm import Session
from src.models.models import Matricula
from src.schemas import MatriculaCreate

# Layer: Service Layer
# This layer contains the business logic for the application.

class MatriculaService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_matriculas(self):
        return self.db.query(Matricula).all()

    def get_matricula_by_id(self, matricula_id: int):
        return self.db.query(Matricula).filter(Matricula.matricula_id == matricula_id).first()

    def create_matricula(self, matricula: MatriculaCreate):
        new_matricula = Matricula(
            estudiante_id=matricula.estudiante_id,
            seccion_id=matricula.seccion_id,
            costo=matricula.costo,
            metodo_pago=matricula.metodo_pago
        )
        self.db.add(new_matricula)
        self.db.commit()
        self.db.refresh(new_matricula)
        return new_matricula