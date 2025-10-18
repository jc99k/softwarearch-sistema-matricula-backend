# src/modules/facultad/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Facultad(Base):
    __tablename__ = 'facultad'
    facultad_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(TEXT)
    ubicacion = Column(String(100))
    decano = Column(String(100))
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    activo = Column(BOOLEAN, default=True)
    carreras = relationship('Carrera', back_populates='facultad')
