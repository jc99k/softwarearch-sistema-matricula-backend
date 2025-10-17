# app.py

from fastapi import FastAPI
from src.database import Base, engine
from src.models import models

# Layer: Application Layer
# This file initializes the FastAPI application and includes the routers.

app = FastAPI(
    title="Sistema de Matricula API",
    description="API for a course registration system",
    version="1.0.0",
)

@app.on_event("startup")
def on_startup():
    # Layer: Persistence Layer
    # Create database tables on startup
    Base.metadata.create_all(bind=engine)

# Layer: Controller Layer
# Include routers for different modules
from src.controllers import estudiante_controller
app.include_router(estudiante_controller.router, prefix="/api/estudiantes", tags=["Estudiantes"])

from src.controllers import profesor_controller
app.include_router(profesor_controller.router, prefix="/api/profesores", tags=["Profesores"])

from src.controllers import facultad_controller
app.include_router(facultad_controller.router, prefix="/api/facultades", tags=["Facultades"])

from src.controllers import carrera_controller
app.include_router(carrera_controller.router, prefix="/api/carreras", tags=["Carreras"])

from src.controllers import curso_controller
app.include_router(curso_controller.router, prefix="/api/cursos", tags=["Cursos"])

from src.controllers import seccion_controller
app.include_router(seccion_controller.router, prefix="/api/secciones", tags=["Secciones"])

from src.controllers import matricula_controller
app.include_router(matricula_controller.router, prefix="/api/matriculas", tags=["Matriculas"])

from src.controllers import pago_controller
app.include_router(pago_controller.router, prefix="/api/pagos", tags=["Pagos"])

from src.controllers import calificacion_controller
app.include_router(calificacion_controller.router, prefix="/api/calificaciones", tags=["Calificaciones"])
