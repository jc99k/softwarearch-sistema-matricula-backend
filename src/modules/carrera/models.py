# src/modules/carrera/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Carrera(Base):
    __tablename__ = 'carrera'
    carrera_id = Column(Integer, primary_key=True)
    facultad_id = Column(Integer, ForeignKey('facultad.facultad_id'), nullable=False, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(TEXT)
    duracion_semestres = Column(Integer, nullable=False)
    titulo_otorgado = Column(String(100))
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    activo = Column(BOOLEAN, default=True)
    facultad = relationship('Facultad', back_populates='carreras')
    cursos = relationship('Curso', back_populates='carrera')
    __table_args__ = (UniqueConstraint('nombre'),)
