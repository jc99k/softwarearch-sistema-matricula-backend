# src/modules/pago/models.py

from sqlalchemy import (Column, Integer, String, Date, TIMESTAMP, BOOLEAN, ForeignKey, UniqueConstraint, CheckConstraint, TEXT, NUMERIC, Index, func)
from sqlalchemy.orm import relationship
from src.database import Base

class Pago(Base):
    __tablename__ = 'pago'
    pago_id = Column(Integer, primary_key=True)
    matricula_id = Column(Integer, ForeignKey('matricula.matricula_id'), nullable=False)
    fecha_pago = Column(Date, nullable=False, server_default=func.now())
    monto = Column(NUMERIC(10, 2), nullable=False)
    metodo_pago = Column(String(50), nullable=False)
    referencia = Column(String(100))
    estado = Column(String(20), nullable=False, default='PROCESADO')
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    matricula = relationship('Matricula', back_populates='pago')
    __table_args__ = (CheckConstraint('monto > 0'), CheckConstraint("estado IN ('PENDIENTE', 'PROCESADO', 'RECHAZADO')"))
