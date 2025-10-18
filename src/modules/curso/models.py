# src/modules/curso/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Curso(Base):
    __tablename__ = 'curso'
    curso_id = Column(Integer, primary_key=True)
    carrera_id = Column(Integer, ForeignKey('carrera.carrera_id'), nullable=False)
    codigo = Column(String(20), unique=True, nullable=False, index=True)
    nombre = Column(String(100), nullable=False, index=True)
    descripcion = Column(TEXT)
    creditos = Column(Integer, nullable=False)
    nivel_semestre = Column(Integer, nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    activo = Column(BOOLEAN, default=True)
    carrera = relationship('Carrera', back_populates='cursos')
    secciones = relationship('Seccion', back_populates='curso')
    prerrequisitos = relationship('Prerrequisito', foreign_keys='Prerrequisito.curso_id', back_populates='curso')
    es_prerrequisito_de = relationship('Prerrequisito', foreign_keys='Prerrequisito.curso_req_id', back_populates='curso_requerido')
    __table_args__ = (CheckConstraint('creditos > 0'), CheckConstraint('nivel_semestre > 0'))

class Prerrequisito(Base):
    __tablename__ = 'prerrequisito'
    prerrequisito_id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey('curso.curso_id', ondelete='CASCADE'), nullable=False)
    curso_req_id = Column(Integer, ForeignKey('curso.curso_id', ondelete='CASCADE'), nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    curso = relationship('Curso', foreign_keys=[curso_id], back_populates='prerrequisitos')
    curso_requerido = relationship('Curso', foreign_keys=[curso_req_id], back_populates='es_prerrequisito_de')
    __table_args__ = (UniqueConstraint('curso_id', 'curso_req_id'), CheckConstraint('curso_id != curso_req_id'))
