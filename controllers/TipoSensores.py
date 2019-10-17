from flask import jsonify, request
from db.db import cnx

class TipoSensor():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM tipo_sensores")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            # Create a zip object from two lists
            registro = dict(zip(columns, row))
            # Create a dictionary from zip object
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create(body):
        #Campos
        data = (body['referencia'],body['nombre'],body['variable'],body['precio'],body['salida'],body['imagen'])
        #Sentencia SQL
        sql = "INSERT INTO tipo_sensores(referencia, nombre, variable, precio, salida, imagen) VALUES(%s, %s, %s, %s, %s, %s)"
        cur.execute(sql,data)        
        cnx.commit()
        return {'estado': "Insertado"}, 200
