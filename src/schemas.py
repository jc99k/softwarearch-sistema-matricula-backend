# src/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    email: str
    telefono: Optional[str] = None
    fecha_nacimiento: date
    direccion: Optional[str] = None

class EstudianteCreate(EstudianteBase):
    pass

class Estudiante(EstudianteBase):
    estudiante_id: int
    activo: bool

    class Config:
        orm_mode = True

class ProfesorBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    email: str
    telefono: Optional[str] = None
    especialidad: Optional[str] = None
    titulo_academico: Optional[str] = None

class ProfesorCreate(ProfesorBase):
    pass

class Profesor(ProfesorBase):
    profesor_id: int
    activo: bool

    class Config:
        orm_mode = True

class FacultadBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None
    decano: Optional[str] = None

class FacultadCreate(FacultadBase):
    pass

class Facultad(FacultadBase):
    facultad_id: int
    activo: bool

    class Config:
        orm_mode = True

class CarreraBase(BaseModel):
    facultad_id: int
    nombre: str
    descripcion: Optional[str] = None
    duracion_semestres: int
    titulo_otorgado: Optional[str] = None

class CarreraCreate(CarreraBase):
    pass

class Carrera(CarreraBase):
    carrera_id: int
    activo: bool

    class Config:
        orm_mode = True

class CursoBase(BaseModel):
    carrera_id: int
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    creditos: int
    nivel_semestre: int

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    curso_id: int
    activo: bool

    class Config:
        orm_mode = True

class SeccionBase(BaseModel):
    curso_id: int
    profesor_id: int
    codigo: str
    capacidad_maxima: int
    aula: Optional[str] = None
    horario: Optional[str] = None
    dias: Optional[str] = None
    periodo_academico: str
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None

class SeccionCreate(SeccionBase):
    pass

class Seccion(SeccionBase):
    seccion_id: int
    activo: bool

    class Config:
        orm_mode = True

class MatriculaBase(BaseModel):
    estudiante_id: int
    seccion_id: int
    costo: float
    metodo_pago: Optional[str] = None

class MatriculaCreate(MatriculaBase):
    pass

class Matricula(MatriculaBase):
    matricula_id: int
    fecha_matricula: date
    estado: str

    class Config:
        orm_mode = True

class PagoBase(BaseModel):
    matricula_id: int
    monto: float
    metodo_pago: str
    referencia: Optional[str] = None

class PagoCreate(PagoBase):
    pass

class Pago(PagoBase):
    pago_id: int
    fecha_pago: date
    estado: str

    class Config:
        orm_mode = True

class CalificacionBase(BaseModel):
    matricula_id: int
    nota: float
    observacion: Optional[str] = None

class CalificacionCreate(CalificacionBase):
    pass

class Calificacion(CalificacionBase):
    calificacion_id: int

    class Config:
        orm_mode = True
