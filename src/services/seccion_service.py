# src/services/seccion_service.py

from sqlalchemy.orm import Session
from src.models.models import Seccion
from src.schemas import SeccionCreate

# Layer: Service Layer
# This layer contains the business logic for the application.

class SeccionService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_secciones(self):
        return self.db.query(Seccion).all()

    def get_seccion_by_id(self, seccion_id: int):
        return self.db.query(Seccion).filter(Seccion.seccion_id == seccion_id).first()

    def create_seccion(self, seccion: SeccionCreate):
        new_seccion = Seccion(
            curso_id=seccion.curso_id,
            profesor_id=seccion.profesor_id,
            codigo=seccion.codigo,
            capacidad_maxima=seccion.capacidad_maxima,
            aula=seccion.aula,
            horario=seccion.horario,
            dias=seccion.dias,
            periodo_academico=seccion.periodo_academico,
            fecha_inicio=seccion.fecha_inicio,
            fecha_fin=seccion.fecha_fin
        )
        self.db.add(new_seccion)
        self.db.commit()
        self.db.refresh(new_seccion)
        return new_seccion