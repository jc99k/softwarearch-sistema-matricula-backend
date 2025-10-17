# src/controllers/calificacion_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.calificacion_service import CalificacionService
from src.schemas import Calificacion, CalificacionCreate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Calificacion])
def get_all_calificaciones(db: Session = Depends(get_db)):
    """
    Retrieve all grades.
    """
    service = CalificacionService(db)
    calificaciones = service.get_all_calificaciones()
    return calificaciones

@router.get("/{calificacion_id}", response_model=Calificacion)
def get_calificacion(calificacion_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single grade by its ID.
    """
    service = CalificacionService(db)
    calificacion = service.get_calificacion_by_id(calificacion_id)
    if calificacion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Calificacion not found")
    return calificacion

@router.post("/", response_model=Calificacion, status_code=status.HTTP_201_CREATED)
def create_calificacion(calificacion: CalificacionCreate, db: Session = Depends(get_db)):
    """
    Create a new grade.
    """
    service = CalificacionService(db)
    new_calificacion = service.create_calificacion(calificacion)
    return new_calificacion