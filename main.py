from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from flask_wtf import FlaskForm
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

app = Flask(__name__)

#   CONEXION Y DESCONEXION A MYSQL
""" def conectar():
    # Configuración de la conexión
    config = {
        'user': 'tu_usuario',
        'password': 'tu_contraseña',
        'host': 'localhost',
        'database': 'tu_base_de_datos',
        'raise_on_warnings': True,
    }
    # Intentar establecer la conexión
    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def desconectar(conexion):
    # Intentar cerrar la conexión
    try:
        conexion.close()
        print("Conexión cerrada correctamente")
    except mysql.connector.Error as err:
        print(f"Error al cerrar la conexión: {err}") """
# Ejemplo de uso
#   conexion_bd = conectar()
    # Realizar operaciones con la base de datos
#   desconectar(conexion_bd)

#   RUTA PAGINA PRINCIPAL
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)