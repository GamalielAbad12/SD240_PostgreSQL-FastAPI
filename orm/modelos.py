from orm.config import BaseClass

from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, Float

import datetime

class Usuario(BaseClass):
    _tablename_ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    email=Column, String(40)
    feha_registro= Column(DateTime(timezone=True), default=datetime.datetime.now)

class Compra(BaseClass):
    _tablename_ = "compras"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey(Usuario.id))
    producto = Column(String(100))
    precio = Column(Float)

class Foto(BaseClass):
    _tablename_ = "fotos"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey(Usuario.id))
    titulo = Column(String(100))
    descripcion = Column(String(100))
    ruta = Column(String(100))
