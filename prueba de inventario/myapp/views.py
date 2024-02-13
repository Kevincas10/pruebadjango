from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from mysql.connector import Error

def buscar_por_id(id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MALUGUCK57',
            database='clinica_dental'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            sql = f"SELECT * FROM material WHERE idMaterial = {id}"
            cursor.execute(sql)

            resultado = cursor.fetchone()

            if resultado:
                return resultado
            else:
                return None
    except Error as e:
        print("Error al conectar a MySQL", e)
        return "Error al conectar a MySQL: " + str(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada.")

def index(request):
    resultados = prog()
    return render(request, 'index.html', {'resultados': resultados})

def buscar(request):
    id = request.GET.get('id')

    if id:
        elemento = buscar_por_id(id)
        if elemento:
            return render(request, 'detalle.html', {'elemento': elemento})
        else:
            return HttpResponse("Elemento no encontrado")
    else:
        return HttpResponse("ID no proporcionado")

def prog():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MALUGUCK57',
            database='clinica_dental'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM material")
            resultados = cursor.fetchall()

            return resultados
    except Error as e:
        print("Error al conectar a MySQL", e)
        return "Error al conectar a MySQL: " + str(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada.")
