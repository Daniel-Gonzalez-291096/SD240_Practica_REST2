# La clase base de las clases modelos
# los modelos o clases modelo son las clases que mapean a las tablas
from orm.config import BaseClass
# Importar de SQLALchemy los tipos de datos que usan las columnas de las tablas
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
# Para que calcular la hora actual
import datetime

# Por convención las clases tienen nombres en singular y comienzan con mayúsculas
# modelo para la tabla 'alumnos'
class Alumno(BaseClass):
    __tablename__ = "alumnos" # Nombre de la tabla en la BD
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    domicilio = Column(String(100))
    carrera = Column(String(100))
    trimestre = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    fecha_registro = Column(DateTime(timezone=True), default=datetime.datetime.now)

# modelo para la tabla 'calificaciones'
class Calificacion(BaseClass):
    __tablename__ = "calificaciones" # Nombre de la tabla en la BD
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id"))
    uea = Column(String(100))
    calificacion = Column(String(100))

# modelo para la tabla 'fotos'
class Foto(BaseClass):
    __tablename__ = "fotos" # Nombre de la tabla en la BD
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id"))
    titulo = Column(String(100))
    descripcion = Column(String(100))
    ruta = Column(String(100))
