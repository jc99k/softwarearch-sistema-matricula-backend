# src/controllers/pago_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.pago_service import PagoService
from src.schemas import Pago, PagoCreate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Pago])
def get_all_pagos(db: Session = Depends(get_db)):
    """
    Retrieve all payments.
    """
    service = PagoService(db)
    pagos = service.get_all_pagos()
    return pagos

@router.get("/{pago_id}", response_model=Pago)
def get_pago(pago_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single payment by its ID.
    """
    service = PagoService(db)
    pago = service.get_pago_by_id(pago_id)
    if pago is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pago not found")
    return pago

@router.post("/", response_model=Pago, status_code=status.HTTP_201_CREATED)
def create_pago(pago: PagoCreate, db: Session = Depends(get_db)):
    """
    Create a new payment.
    """
    service = PagoService(db)
    new_pago = service.create_pago(pago)
    return new_pago