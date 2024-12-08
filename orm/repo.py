from sqlalchemy.orm import Session
import orm.modelos as modelos

#----------------------------------------funciones SELECT--------------------------------------------#

#-----SELECT * FROM app.alumnos-----
# para obtener todos los alumnos
def lista_alumnos(sesion: Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

#-----SELECT * FROM app.alumnos WHERE id={id_al-----
# para obtener un alumno por ID
def alumno_por_id(sesion: Session, id_alumno: int):
    print("SELECT * FROM app.alumnos WHERE id=",id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()

#-----SELECT * FROM app.fotos-----
# para obtener todas las fotos de un alumno
def fotos_por_id_alumno(sesion: Session, id_alumno: int):
    print("ELECT * FROM app.fotos where id=", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_alumno).all()

#-----SELECT * FROM app.fotos WHERE id={id_fo}-----
# para obtener una foto por su ID
def foto_por_id(sesion: Session, id_foto: int):
    print("SELECT * FROM app.fotos WHERE id=",id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()

#-----SELECT * FROM app.calificaciones-----
# para obtener todas las calificaciones de un alumno
def calificaciones_por_id_alumno(sesion: Session, id_alumno: int):
    print("SELECT * FROM app.calificaciones where id =",id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_alumno).all()

#-----SELECT * FROM app.calificaciones WHERE id={id_fo}-----
# para obtener una calificacion por su ID
def calificacion_por_id(sesion: Session, id_calificacion: int):
    print("SELECT * FROM app.calificaciones WHERE id=",id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()

#----------------------------------------funciones DELETE--------------------------------------------#

#-----DELETE FROM app.alumnos WHERE id={id_al}-----
# para eliminar un alumno por ID
def borrar_alumno_por_id(sesion: Session, id_alumno: int):
    print("DELETE FROM app.alumnos WHERE id=",id_alumno)
    alumno = alumno_por_id(sesion, id_alumno)
    if alumno is not None:
        sesion.delete(alumno)
        sesion.commit()

#-----DELETE FROM app.calificaciones WHERE id_alumnos={id_al}-----
# para eliminar todas las calificaciones de un alumno
def borrar_calificaciones_por_id_alumno(sesion: Session, id_alumno: int):
    print("DELETE FROM app.calificaciones WHERE id_alumnos=",id_alumno)
    calificaciones = calificaciones_por_id_alumno(sesion, id_alumno)
    for calificacion in calificaciones:
        sesion.delete(calificacion)
    sesion.commit()

#-----DELETE FROM app.fotos WHERE id_alumnos={id_al}-----
# para eliminar todas las fotos de un alumno
def borrar_fotos_por_id_alumno(sesion: Session, id_alumno: int):
    print("DELETE FROM app.fotos WHERE id_alumnos=", id_alumno)
    fotos = fotos_por_id_alumno(sesion, id_alumno)
    for foto in fotos:
        sesion.delete(foto)
    sesion.commit()

#-----------------------------funciones DELETE en especifico-----------------------------------------#


#-----DELETE FROM app.calificaciones WHERE id = {id_calificacion}-----
# elimina una calificacion por su ID especifico
def borrar_calificacion_por_id(sesion: Session, id_calificacion: int):
    print("DELETE FROM app.calificaciones WHERE id =", id_calificacion)
    calificacion = calificacion_por_id(sesion, id_calificacion)
    if calificacion is not None:
        sesion.delete(calificacion)
        sesion.commit()
        return {"mensaje": f"calificacion con id {id_calificacion} eliminada"}
    return {"error": f"no se encontro la calificacion con id {id_calificacion}."}

#-----DELETE FROM app.fotos WHERE id = :id_foto-----
# elimina una foto por su ID especifico
def borrar_foto_por_id(sesion: Session, id_foto: int):
    print("DELETE FROM app.fotos WHERE id =", id_foto)
    foto = foto_por_id(sesion, id_foto)
    if foto is not None:
        sesion.delete(foto)
        sesion.commit()
        return {"mensaje": f"foto con id {id_foto} eliminada"}
    return {"error": f"no se encontro la foto con id {id_foto}."}


