#El enine permite configurar la conexión a la DB
from sqlalchemy import create_engine
#El session maker permite crear sesiones para hacer consultas
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



#1 Configurar la conexión BD 
# servidorBD://usuario:passrord@url:puerto/nombreBD
URL_BASE_DATOS = "postgresql://gamalielabad:09082002@localhost:5432/base_ejemplo"
# conectados mediante el esquema app
engine = create_engine(URL_BASE_DATOS,
                       connect_args={
                           "options": "-csearch_path=app"                           
                       })
SessionClass = sessionmaker(engine)

def generador_sesion():
    sesion = SessionClass()
    try: 
        yield sesion
    finally: 
        sesion.close()

#3.- Obtener la clase base para mapear tablas 
BaseClass = declarative_base()


