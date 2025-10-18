# src/modules/estudiante/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Estudiante(Base):
    __tablename__ = 'estudiante'
    estudiante_id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False, index=True)
    dni = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20))
    fecha_nacimiento = Column(Date, nullable=False)
    direccion = Column(String(200))
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    activo = Column(BOOLEAN, default=True)
    matriculas = relationship('Matricula', back_populates='estudiante')
