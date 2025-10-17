# src/controllers/carrera_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.carrera_service import CarreraService
from src.schemas import Carrera, CarreraCreate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Carrera])
def get_all_carreras(db: Session = Depends(get_db)):
    """
    Retrieve all careers.
    """
    service = CarreraService(db)
    carreras = service.get_all_carreras()
    return carreras

@router.get("/{carrera_id}", response_model=Carrera)
def get_carrera(carrera_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single career by its ID.
    """
    service = CarreraService(db)
    carrera = service.get_carrera_by_id(carrera_id)
    if carrera is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrera not found")
    return carrera

@router.post("/", response_model=Carrera, status_code=status.HTTP_201_CREATED)
def create_carrera(carrera: CarreraCreate, db: Session = Depends(get_db)):
    """
    Create a new career.
    """
    service = CarreraService(db)
    new_carrera = service.create_carrera(carrera)
    return new_carrera