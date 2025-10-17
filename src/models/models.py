'''# src/models/models.py

from src.db import db
from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index)
from sqlalchemy.orm import relationship

# Layer: Model Layer
# The models below represent the data structure of the application and interact with the database.

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    estudiante_id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False, index=True)
    dni = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20))
    fecha_nacimiento = Column(Date, nullable=False)
    direccion = Column(String(200))
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    activo = Column(BOOLEAN, default=True)
    matriculas = relationship('Matricula', back_populates='estudiante')

class Profesor(db.Model):
    __tablename__ = 'profesor'
    profesor_id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False, index=True)
    dni = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20))
    especialidad = Column(String(100))
    titulo_academico = Column(String(100))
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    activo = Column(BOOLEAN, default=True)
    secciones = relationship('Seccion', back_populates='profesor')

class Facultad(db.Model):
    __tablename__ = 'facultad'
    facultad_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(TEXT)
    ubicacion = Column(String(100))
    decano = Column(String(100))
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    activo = Column(BOOLEAN, default=True)
    carreras = relationship('Carrera', back_populates='facultad')

class Carrera(db.Model):
    __tablename__ = 'carrera'
    carrera_id = Column(Integer, primary_key=True)
    facultad_id = Column(Integer, ForeignKey('facultad.facultad_id'), nullable=False, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(TEXT)
    duracion_semestres = Column(Integer, nullable=False)
    titulo_otorgado = Column(String(100))
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    activo = Column(BOOLEAN, default=True)
    facultad = relationship('Facultad', back_populates='carreras')
    cursos = relationship('Curso', back_populates='carrera')
    __table_args__ = (UniqueConstraint('nombre'),)

class Curso(db.Model):
    __tablename__ = 'curso'
    curso_id = Column(Integer, primary_key=True)
    carrera_id = Column(Integer, ForeignKey('carrera.carrera_id'), nullable=False)
    codigo = Column(String(20), unique=True, nullable=False, index=True)
    nombre = Column(String(100), nullable=False, index=True)
    descripcion = Column(TEXT)
    creditos = Column(Integer, nullable=False)
    nivel_semestre = Column(Integer, nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    activo = Column(BOOLEAN, default=True)
    carrera = relationship('Carrera', back_populates='cursos')
    secciones = relationship('Seccion', back_populates='curso')
    prerrequisitos = relationship('Prerrequisito', foreign_keys='Prerrequisito.curso_id', back_populates='curso')
    es_prerrequisito_de = relationship('Prerrequisito', foreign_keys='Prerrequisito.curso_req_id', back_populates='curso_requerido')
    __table_args__ = (CheckConstraint('creditos > 0'), CheckConstraint('nivel_semestre > 0'))

class Prerrequisito(db.Model):
    __tablename__ = 'prerrequisito'
    prerrequisito_id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey('curso.curso_id', ondelete='CASCADE'), nullable=False)
    curso_req_id = Column(Integer, ForeignKey('curso.curso_id', ondelete='CASCADE'), nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    curso = relationship('Curso', foreign_keys=[curso_id], back_populates='prerrequisitos')
    curso_requerido = relationship('Curso', foreign_keys=[curso_req_id], back_populates='es_prerrequisito_de')
    __table_args__ = (UniqueConstraint('curso_id', 'curso_req_id'), CheckConstraint('curso_id != curso_req_id'))

class Seccion(db.Model):
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
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    activo = Column(BOOLEAN, default=True)
    curso = relationship('Curso', back_populates='secciones')
    profesor = relationship('Profesor', back_populates='secciones')
    matriculas = relationship('Matricula', back_populates='seccion')
    __table_args__ = (UniqueConstraint('curso_id', 'codigo', 'periodo_academico'), CheckConstraint('capacidad_maxima > 0'))

class Matricula(db.Model):
    __tablename__ = 'matricula'
    matricula_id = Column(Integer, primary_key=True)
    estudiante_id = Column(Integer, ForeignKey('estudiante.estudiante_id'), nullable=False, index=True)
    seccion_id = Column(Integer, ForeignKey('seccion.seccion_id'), nullable=False, index=True)
    fecha_matricula = Column(Date, nullable=False, server_default=db.func.current_date())
    estado = Column(String(20), nullable=False, default='PENDIENTE')
    costo = Column(NUMERIC(10, 2), nullable=False)
    metodo_pago = Column(String(50))
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    estudiante = relationship('Estudiante', back_populates='matriculas')
    seccion = relationship('Seccion', back_populates='matriculas')
    pago = relationship('Pago', back_populates='matricula', uselist=False)
    calificacion = relationship('Calificacion', back_populates='matricula', uselist=False)
    __table_args__ = (UniqueConstraint('estudiante_id', 'seccion_id'), CheckConstraint("estado IN ('PENDIENTE', 'PAGADO', 'ANULADO', 'COMPLETADO')"), CheckConstraint('costo >= 0'))

class Pago(db.Model):
    __tablename__ = 'pago'
    pago_id = Column(Integer, primary_key=True)
    matricula_id = Column(Integer, ForeignKey('matricula.matricula_id'), nullable=False)
    fecha_pago = Column(Date, nullable=False, server_default=db.func.current_date())
    monto = Column(NUMERIC(10, 2), nullable=False)
    metodo_pago = Column(String(50), nullable=False)
    referencia = Column(String(100))
    estado = Column(String(20), nullable=False, default='PROCESADO')
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    matricula = relationship('Matricula', back_populates='pago')
    __table_args__ = (CheckConstraint('monto > 0'), CheckConstraint("estado IN ('PENDIENTE', 'PROCESADO', 'RECHAZADO')"))

class Calificacion(db.Model):
    __tablename__ = 'calificacion'
    calificacion_id = Column(Integer, primary_key=True)
    matricula_id = Column(Integer, ForeignKey('matricula.matricula_id'), nullable=False, unique=True)
    nota = Column(NUMERIC(5, 2))
    observacion = Column(TEXT)
    fecha_registro = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    matricula = relationship('Matricula', back_populates='calificacion')
    __table_args__ = (CheckConstraint('nota >= 0 AND nota <= 20'),)
'''