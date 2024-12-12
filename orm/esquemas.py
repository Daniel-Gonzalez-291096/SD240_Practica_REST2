from pydantic import BaseModel
from typing import Optional

# Esquema para Alumnos
class AlumnoBase(BaseModel):
    nombre: str
    edad: int
    domicilio: str 
    carrera: str
    trimestre: str
    email: str
    password: str

# Esquema para Calificaciones
class CalificacionesBase(BaseModel):
    uea: str
    calificacion: str


# Esquema para Fotos
class FotoBase(BaseModel):
    titulo: str
    descripcion: str
