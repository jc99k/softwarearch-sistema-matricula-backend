# app.py

from fastapi import FastAPI
from src.database import Base, engine
# from src.models import models # This import is no longer needed as models are now in modules

# Import all models from their respective modules to ensure Base.metadata.create_all discovers them
from src.modules.estudiante import models as estudiante_models
from src.modules.profesor import models as profesor_models
from src.modules.facultad import models as facultad_models
from src.modules.carrera import models as carrera_models
from src.modules.curso import models as curso_models
from src.modules.seccion import models as seccion_models
from src.modules.matricula import models as matricula_models
from src.modules.pago import models as pago_models
from src.modules.calificacion import models as calificacion_models


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
from src.modules.estudiante import controllers as estudiante_controller
app.include_router(estudiante_controller.router, prefix="/api/estudiantes", tags=["Estudiantes"])

from src.modules.profesor import controllers as profesor_controller
app.include_router(profesor_controller.router, prefix="/api/profesores", tags=["Profesores"])

from src.modules.facultad import controllers as facultad_controller
app.include_router(facultad_controller.router, prefix="/api/facultades", tags=["Facultades"])

from src.modules.carrera import controllers as carrera_controller
app.include_router(carrera_controller.router, prefix="/api/carreras", tags=["Carreras"])

from src.modules.curso import controllers as curso_controller
app.include_router(curso_controller.router, prefix="/api/cursos", tags=["Cursos"])

from src.modules.seccion import controllers as seccion_controller
app.include_router(seccion_controller.router, prefix="/api/secciones", tags=["Secciones"])

from src.modules.matricula import controllers as matricula_controller
app.include_router(matricula_controller.router, prefix="/api/matriculas", tags=["Matriculas"])

from src.modules.pago import controllers as pago_controller
app.include_router(pago_controller.router, prefix="/api/pagos", tags=["Pagos"])

from src.modules.calificacion import controllers as calificacion_controller
app.include_router(calificacion_controller.router, prefix="/api/calificaciones", tags=["Calificaciones"])
