from fastapi import FastAPI, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
import orm.repo as repo #funciones para hacer consultas a la BD
from orm.config import generador_sesion  #generador de sesiones


# creacion del servidor
app = FastAPI()

# decorator
@app.get("/")
def bienvenida():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "Bienvenid@ a la API de alumnos de la practica REST"
    }

    return respuesta

# para obtener todos los alumnos
@app.get("/alumnos")
def listar_alumnos(sesion: Session = Depends(generador_sesion)):
    print("Api consultando alumnos")
    return repo.lista_alumnos(sesion)

# para btener un alumno por ID
@app.get("/alumnos/{id}")
def obtener_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

# para pbtener todas las calificaciones de un alumnos
@app.get("/alumnos/{id}/calificaciones")
def obtener_calificaciones(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando calificaciones de alumnos")
    return repo.calificaciones_por_id_alumno(sesion, id)

# para obtener todas las fotos de un alumno
@app.get("/alumnos/{id}/fotos")
def obtener_fotos(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando fotos de un alumno")
    return repo.fotos_por_id_alumno(sesion, id)

# para obtener una foto por ID
@app.get("/fotos/{id}")
def obtener_foto(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando foto por id")
    return repo.foto_por_id(sesion, id)

# para obtener una calificacion por ID
@app.get("/calificaciones/{id}")
def obtener_calificacion(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando calificacion por id")
    return repo.calificacion_por_id(sesion, id)

# para eliminar una foto por ID
@app.delete("/fotos/{id}")
def eliminar_foto(id: int, sesion: Session = Depends(generador_sesion)):
    repo.borrar_foto_por_id(sesion, id)
    return {"foto_borrada", "ok"}

# para eliminar una calificacion por ID
@app.delete("/calificaciones/{id}")
def eliminar_calificacion(id: int, sesion: Session = Depends(generador_sesion)):
    repo.borrar_calificacion_por_id(sesion, id)
    return {"calificacion_borrada", "ok"}

# para eliminr todas las calificaciones de un alumno
@app.delete("/alumnos/{id}/calificaciones")
def eliminar_calificaciones_por_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion, id)
    return {"mensaje": f"calificaciones del alumno con id {id} fueron eliminadas"}

# para eliminar todas las fotos de un alumno
@app.delete("/alumnos/{id}/fotos")
def eliminar_fotos_por_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion, id)
    return {"mensaje": f"fotos del alumno con id {id} eliminadas"}

# para eiminar un alumno (y ademas de sus datos relacionados)
@app.delete("/alumnos/{id}")
def eliminar_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion, id)
    repo.borrar_calificaciones_por_id_alumno(sesion, id)
    repo.borrar_alumno_por_id(sesion, id)
    return {"mensaje": f"alumno con id {id} eliminado"}