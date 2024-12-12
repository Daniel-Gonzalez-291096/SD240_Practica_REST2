from sqlalchemy.orm import Session
import orm.modelos as modelos
import orm.esquemas as esquemas

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

#---------------------------------------Practica REST 2----------------------------------------------------#

#---post("/alumnos”)---#
def crear_alumno(sesion:Session, alumno_nuevo: esquemas.AlumnoBase):
    alumno_bd = modelos.Alumno()
    
    alumno_bd.nombre = alumno_nuevo.nombre
    alumno_bd.edad = alumno_nuevo.edad
    alumno_bd.domicilio = alumno_nuevo.domicilio
    alumno_bd.carrera = alumno_nuevo.carrera
    alumno_bd.trimestre = alumno_nuevo.trimestre
    alumno_bd.email = alumno_nuevo.email
    alumno_bd.password = alumno_nuevo.password        
    
    sesion.add(alumno_bd)
    sesion.commit()
    sesion.refresh(alumno_bd)
    return alumno_bd

#---put("/alumnos/{id})---#
def actualizar_alumno(sesion: Session, id_alumno: int, alumno_esquema = esquemas.AlumnoBase):
    alumno_bd = alumno_por_id(sesion, id_alumno)
    if alumno_bd is not None:
        alumno_bd.nombre = alumno_esquema.nombre
        alumno_bd.edad = alumno_esquema.edad
        alumno_bd.domicilio = alumno_esquema.domicilio
        alumno_bd.carrera = alumno_esquema.carrera
        alumno_bd.trimestre = alumno_esquema.trimestre
        alumno_bd.email = alumno_esquema.email
        alumno_bd.password = alumno_esquema.password  
        
        sesion.commit()
        sesion.refresh(alumno_bd)
        return alumno_esquema
    else:
        return  {"mensaje":"No existe el alumno"}
        

#---post("/alumnos/{id}/calificaciones")---#
def crear_calificacion(sesion: Session, id_alumno: int, calificacion_esquema: esquemas.CalificacionesBase):
    calificacion_bd = modelos.Calificacion(
        id_alumno=id_alumno,
        uea=calificacion_esquema.uea,
        calificacion=calificacion_esquema.calificacion
    )
    sesion.add(calificacion_bd)
    sesion.commit()
    sesion.refresh(calificacion_bd)
    return calificacion_bd

#---put("/calificaciones/{id})---#
def actualizar_calificacion(sesion: Session, id_calificacion: int, calificacion_esquema: esquemas.CalificacionesBase):
    calificacion_bd = sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()
    if calificacion_bd is not None:
        if calificacion_esquema.uea: 
            #para saber si el valor de la uea esta presente
            calificacion_bd.uea = calificacion_esquema.uea
        if calificacion_esquema.calificacion: 
            #mismo caso para saber si el valor de la calificación esta presente
            calificacion_bd.calificacion = calificacion_esquema.calificacion
        sesion.commit()
        sesion.refresh(calificacion_bd)
        return calificacion_bd
    else:
        return {"mensaje": "no existe la calificacion"}
    
#---post("/alumnos/{id}/fotos")---#
def crear_foto(sesion: Session, id_alumno: int, foto_esquema: esquemas.FotoBase):
    foto_bd = modelos.Foto(
        id_alumno=id_alumno,
        titulo=foto_esquema.titulo,
        descripcion=foto_esquema.descripcion
    )
    sesion.add(foto_bd)
    sesion.commit()
    sesion.refresh(foto_bd)
    return foto_bd

#---put("/fotos/{id}")---#
def actualizar_foto(sesion: Session, id_foto: int, foto_esquema: esquemas.FotoBase):
    foto_bd = sesion.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()
    if foto_bd is not None:
        if foto_esquema.titulo: foto_bd.titulo = foto_esquema.titulo
        if foto_esquema.descripcion: foto_bd.descripcion = foto_esquema.descripcion
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        return {"mensaje": "no existe la foto"}
