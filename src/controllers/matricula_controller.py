# src/controllers/matricula_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.matricula_service import MatriculaService
from src.schemas import Matricula, MatriculaCreate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Matricula])
def get_all_matriculas(db: Session = Depends(get_db)):
    """
    Retrieve all enrollments.
    """
    service = MatriculaService(db)
    matriculas = service.get_all_matriculas()
    return matriculas

@router.get("/{matricula_id}", response_model=Matricula)
def get_matricula(matricula_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single enrollment by its ID.
    """
    service = MatriculaService(db)
    matricula = service.get_matricula_by_id(matricula_id)
    if matricula is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matricula not found")
    return matricula

@router.post("/", response_model=Matricula, status_code=status.HTTP_201_CREATED)
def create_matricula(matricula: MatriculaCreate, db: Session = Depends(get_db)):
    """
    Create a new enrollment.
    """
    service = MatriculaService(db)
    new_matricula = service.create_matricula(matricula)
    return new_matricula