# src/controllers/curso_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.curso_service import CursoService
from src.schemas import Curso, CursoCreate, CursoUpdate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Curso])
def get_all_cursos(db: Session = Depends(get_db)):
    """
    Retrieve all courses.
    """
    service = CursoService(db)
    cursos = service.get_all_cursos()
    return cursos

@router.get("/{curso_id}", response_model=Curso)
def get_curso(curso_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single course by its ID.
    """
    service = CursoService(db)
    curso = service.get_curso_by_id(curso_id)
    if curso is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso not found")
    return curso

@router.post("/", response_model=Curso, status_code=status.HTTP_201_CREATED)
def create_curso(curso: CursoCreate, db: Session = Depends(get_db)):
    """
    Create a new course.
    """
    service = CursoService(db)
    new_curso = service.create_curso(curso)
    return new_curso

@router.put("/{curso_id}", response_model=Curso)
def update_curso(curso_id: int, curso_data: CursoUpdate, db: Session = Depends(get_db)):
    """
    Update an existing course.
    """
    service = CursoService(db)
    updated_curso = service.update_curso(curso_id, curso_data)
    if updated_curso is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso not found")
    return updated_curso

@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    """
    Delete a course.
    """
    service = CursoService(db)
    deleted_curso = service.delete_curso(curso_id)
    if deleted_curso is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso not found")
    return
