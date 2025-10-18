# src/modules/seccion/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Seccion(Base):
    __tablename__ = 'seccion'
    seccion_id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey('curso.curso_id'), nullable=False, index=True)
    profesor_id = Column(Integer, ForeignKey('profesor.profesor_id'), nullable=False, index=True)
    codigo = Column(String(20), nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    aula = Column(String(50))
    horario = Column(String(50))
    dias = Column(String(50))
    periodo_academico = Column(String(20), nullable=False, index=True)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    activo = Column(BOOLEAN, default=True)
    curso = relationship('Curso', back_populates='secciones')
    profesor = relationship('Profesor', back_populates='secciones')
    matriculas = relationship('Matricula', back_populates='seccion')
    __table_args__ = (UniqueConstraint('curso_id', 'codigo', 'periodo_academico'), CheckConstraint('capacidad_maxima > 0'))
