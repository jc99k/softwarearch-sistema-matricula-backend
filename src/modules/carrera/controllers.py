# src/controllers/carrera_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...database import get_db
from .services import CarreraService
from .schemas import Carrera, CarreraCreate, CarreraUpdate

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

@router.put("/{carrera_id}", response_model=Carrera)
def update_carrera(carrera_id: int, carrera_data: CarreraUpdate, db: Session = Depends(get_db)):
    """
    Update an existing career.
    """
    service = CarreraService(db)
    updated_carrera = service.update_carrera(carrera_id, carrera_data)
    if updated_carrera is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrera not found")
    return updated_carrera

@router.delete("/{carrera_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrera(carrera_id: int, db: Session = Depends(get_db)):
    """
    Delete a career.
    """
    service = CarreraService(db)
    deleted_carrera = service.delete_carrera(carrera_id)
    if deleted_carrera is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrera not found")
    return
