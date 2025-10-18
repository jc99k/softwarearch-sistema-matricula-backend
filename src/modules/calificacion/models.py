# src/modules/calificacion/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Calificacion(Base):
    __tablename__ = 'calificacion'
    calificacion_id = Column(Integer, primary_key=True)
    matricula_id = Column(Integer, ForeignKey('matricula.matricula_id'), nullable=False, unique=True)
    nota = Column(NUMERIC(5, 2))
    observacion = Column(TEXT)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    matricula = relationship('Matricula', back_populates='calificacion')
    __table_args__ = (CheckConstraint('nota >= 0 AND nota <= 20'),)
