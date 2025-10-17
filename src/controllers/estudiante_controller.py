# src/controllers/estudiante_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.estudiante_service import EstudianteService
from src.schemas import Estudiante, EstudianteCreate, EstudianteUpdate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Estudiante])
def get_all_estudiantes(db: Session = Depends(get_db)):
    """
    Retrieve all students.
    """
    service = EstudianteService(db)
    estudiantes = service.get_all_estudiantes()
    return estudiantes

@router.get("/{estudiante_id}", response_model=Estudiante)
def get_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single student by their ID.
    """
    service = EstudianteService(db)
    estudiante = service.get_estudiante_by_id(estudiante_id)
    if estudiante is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante not found")
    return estudiante

@router.post("/", response_model=Estudiante, status_code=status.HTTP_201_CREATED)
def create_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    """
    Create a new student.
    """
    service = EstudianteService(db)
    new_estudiante = service.create_estudiante(estudiante)
    return new_estudiante

@router.put("/{estudiante_id}", response_model=Estudiante)
def update_estudiante(estudiante_id: int, estudiante_data: EstudianteUpdate, db: Session = Depends(get_db)):
    """
    Update an existing student.
    """
    service = EstudianteService(db)
    updated_estudiante = service.update_estudiante(estudiante_id, estudiante_data)
    if updated_estudiante is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante not found")
    return updated_estudiante

@router.delete("/{estudiante_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    """
    Delete a student.
    """
    service = EstudianteService(db)
    deleted_estudiante = service.delete_estudiante(estudiante_id)
    if deleted_estudiante is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante not found")
    return
