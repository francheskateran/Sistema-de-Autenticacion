import mysql.connector

def obtener_conexion():
    config = {
        'user': 'Andreyfm',
        'password': 'ClubABMF1234',
        'host': 'Andreyfm.mysql.pythonanywhere-services.com',
        'database': 'Andreyfm$default'
    }
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None