# src/controllers/profesor_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...database import get_db
from .services import ProfesorService
from .schemas import Profesor, ProfesorCreate, ProfesorUpdate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Profesor])
def get_all_profesores(db: Session = Depends(get_db)):
    """
    Retrieve all professors.
    """
    service = ProfesorService(db)
    profesores = service.get_all_profesores()
    return profesores

@router.get("/{profesor_id}", response_model=Profesor)
def get_profesor(profesor_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single professor by their ID.
    """
    service = ProfesorService(db)
    profesor = service.get_profesor_by_id(profesor_id)
    if profesor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor not found")
    return profesor

@router.post("/", response_model=Profesor, status_code=status.HTTP_201_CREATED)
def create_profesor(profesor: ProfesorCreate, db: Session = Depends(get_db)):
    """
    Create a new professor.
    """
    service = ProfesorService(db)
    new_profesor = service.create_profesor(profesor)
    return new_profesor

@router.put("/{profesor_id}", response_model=Profesor)
def update_profesor(profesor_id: int, profesor_data: ProfesorUpdate, db: Session = Depends(get_db)):
    """
    Update an existing professor.
    """
    service = ProfesorService(db)
    updated_profesor = service.update_profesor(profesor_id, profesor_data)
    if updated_profesor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor not found")
    return updated_profesor

@router.delete("/{profesor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profesor(profesor_id: int, db: Session = Depends(get_db)):
    """
    Delete a professor.
    """
    service = ProfesorService(db)
    deleted_profesor = service.delete_profesor(profesor_id)
    if deleted_profesor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor not found")
    return
