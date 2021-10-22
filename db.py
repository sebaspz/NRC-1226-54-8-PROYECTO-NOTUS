import sqlite3
from sqlite3 import Error
from flask import g


def get_db():
    """Función que crea una conexión a la base de datos.

    Parameters:
    Ninguno

    Returns:
    g.db:Retorna la conexión en la variable gloabl g de flask

   """

    try:

        if 'db' not in g:
            g.db = sqlite3.connect('NOTUS_project.db')
        return g.db

    except Error:
        print('error en Base de Datos: '+Error)


def close_db():
    """Función que cierra conexión a la base de datos.

    Parameters:
    Ninguno

    Returns:
    Nada

   """

    db = g.pop('db',None)

    if db is not None:

        db.close()