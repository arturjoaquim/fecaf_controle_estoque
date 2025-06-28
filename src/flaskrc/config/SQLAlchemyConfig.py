from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Engine, event
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass

sql_alchemy = SQLAlchemy(model_class=Base)

@event.listens_for(Engine, "connect")
def habilitar_foreing_keys_sqlite(dbapi_connection, connection_record) -> None:
    """
    Ativa o suporte a Foreign Keys no SQLite.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
