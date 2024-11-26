import orm.modelos as modelos
from sqlalchemy.orm import Session

def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

def compras_por_id(sesion:Session,id_compras:int):
    print("select * from app.compras where id = ", id_compras)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compras).first()

def fotos_por_id(sesion:Session,id_fotos:int):
    print("select * from app.fotos where id = ", id_fotos)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_fotos).first()