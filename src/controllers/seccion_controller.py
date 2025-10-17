# src/controllers/seccion_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.services.seccion_service import SeccionService
from src.schemas import Seccion, SeccionCreate, SeccionUpdate

# Layer: Controller Layer
# This layer handles the HTTP requests and responses, interacting with the service layer.

router = APIRouter()

@router.get("/", response_model=List[Seccion])
def get_all_secciones(db: Session = Depends(get_db)):
    """
    Retrieve all sections.
    """
    service = SeccionService(db)
    secciones = service.get_all_secciones()
    return secciones

@router.get("/{seccion_id}", response_model=Seccion)
def get_seccion(seccion_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single section by its ID.
    """
    service = SeccionService(db)
    seccion = service.get_seccion_by_id(seccion_id)
    if seccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seccion not found")
    return seccion

@router.post("/", response_model=Seccion, status_code=status.HTTP_201_CREATED)
def create_seccion(seccion: SeccionCreate, db: Session = Depends(get_db)):
    """
    Create a new section.
    """
    service = SeccionService(db)
    new_seccion = service.create_seccion(seccion)
    return new_seccion

@router.put("/{seccion_id}", response_model=Seccion)
def update_seccion(seccion_id: int, seccion_data: SeccionUpdate, db: Session = Depends(get_db)):
    """
    Update an existing section.
    """
    service = SeccionService(db)
    updated_seccion = service.update_seccion(seccion_id, seccion_data)
    if updated_seccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seccion not found")
    return updated_seccion

@router.delete("/{seccion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_seccion(seccion_id: int, db: Session = Depends(get_db)):
    """
    Delete a section.
    """
    service = SeccionService(db)
    deleted_seccion = service.delete_seccion(seccion_id)
    if deleted_seccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seccion not found")
    return
