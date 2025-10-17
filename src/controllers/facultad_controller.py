# src/controllers/facultad_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.facultad_service import FacultadService
from src.schemas import Facultad, FacultadCreate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Facultad])
def get_all_facultades(db: Session = Depends(get_db)):
    """
    Retrieve all faculties.
    """
    service = FacultadService(db)
    facultades = service.get_all_facultades()
    return facultades

@router.get("/{facultad_id}", response_model=Facultad)
def get_facultad(facultad_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single faculty by its ID.
    """
    service = FacultadService(db)
    facultad = service.get_facultad_by_id(facultad_id)
    if facultad is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad not found")
    return facultad

@router.post("/", response_model=Facultad, status_code=status.HTTP_201_CREATED)
def create_facultad(facultad: FacultadCreate, db: Session = Depends(get_db)):
    """
    Create a new faculty.
    """
    service = FacultadService(db)
    new_facultad = service.create_facultad(facultad)
    return new_facultad