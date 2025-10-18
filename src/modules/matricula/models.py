# src/modules/matricula/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Matricula(Base):
    __tablename__ = 'matricula'
    matricula_id = Column(Integer, primary_key=True)
    estudiante_id = Column(Integer, ForeignKey('estudiante.estudiante_id'), nullable=False, index=True)
    seccion_id = Column(Integer, ForeignKey('seccion.seccion_id'), nullable=False, index=True)
    fecha_matricula = Column(Date, nullable=False, server_default=func.now())
    estado = Column(String(20), nullable=False, default='PENDIENTE')
    costo = Column(NUMERIC(10, 2), nullable=False)
    metodo_pago = Column(String(50))
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    estudiante = relationship('Estudiante', back_populates='matriculas')
    seccion = relationship('Seccion', back_populates='matriculas')
    pago = relationship('Pago', back_populates='matricula', uselist=False)
    calificacion = relationship('Calificacion', back_populates='matricula', uselist=False)
    __table_args__ = (UniqueConstraint('estudiante_id', 'seccion_id'), CheckConstraint("estado IN ('PENDIENTE', 'PAGADO', 'ANULADO', 'COMPLETADO')"), CheckConstraint('costo >= 0'))
