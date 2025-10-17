# src/controllers/facultad_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.facultad_service import FacultadService
from src.schemas import Facultad, FacultadCreate, FacultadUpdate

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

@router.put("/{facultad_id}", response_model=Facultad)
def update_facultad(facultad_id: int, facultad_data: FacultadUpdate, db: Session = Depends(get_db)):
    """
    Update an existing faculty.
    """
    service = FacultadService(db)
    updated_facultad = service.update_facultad(facultad_id, facultad_data)
    if updated_facultad is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad not found")
    return updated_facultad

@router.delete("/{facultad_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_facultad(facultad_id: int, db: Session = Depends(get_db)):
    """
    Delete a faculty.
    """
    service = FacultadService(db)
    deleted_facultad = service.delete_facultad(facultad_id)
    if deleted_facultad is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad not found")
    return
