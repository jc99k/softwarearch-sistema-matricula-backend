# src/controllers/pago_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...database import get_db
from .services import PagoService
from .schemas import Pago, PagoCreate, PagoUpdate

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

@router.put("/{pago_id}", response_model=Pago)
def update_pago(pago_id: int, pago_data: PagoUpdate, db: Session = Depends(get_db)):
    """
    Update an existing payment.
    """
    service = PagoService(db)
    updated_pago = service.update_pago(pago_id, pago_data)
    if updated_pago is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pago not found")
    return updated_pago

@router.delete("/{pago_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pago(pago_id: int, db: Session = Depends(get_db)):
    """
    Delete a payment.
    """
    service = PagoService(db)
    deleted_pago = service.delete_pago(pago_id)
    if deleted_pago is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pago not found")
    return
