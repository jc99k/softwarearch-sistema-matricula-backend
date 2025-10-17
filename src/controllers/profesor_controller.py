# src/controllers/profesor_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.profesor_service import ProfesorService
from src.schemas import Profesor, ProfesorCreate

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