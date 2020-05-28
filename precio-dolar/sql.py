
# Creamos el archivo sql.py

# Importamos los paquetes que usaremos
import sqlite3
import name # Nuestro script anterior
import datetime


def s():
    # Variables costantes
    hoy = int(datetime.datetime.now().timestamp()) # obtenemos la fecha actual en formato unix
    # crear tabla EXCHANGES si no existe en la base de datos (BD)
    crear_tabla = "CREATE TABLE IF NOT EXISTS exchanges(last_update INTEGER NOT NULL UNIQUE, day TEXT NOT NULL, rate NUMERIC NOT NULL, next_update INTEGER NOT NULL);"
    # creamos un query para obtener datos de la BD
    get = 'SELECT day, rate, next_update FROM exchanges'

    # Trabajamos en la base de datos local
    try:
        conexion = sqlite3.connect('storage.sqlite') # conexion a la base de datos; si no existe sera creada donde tenemos el script
        puntero = conexion.cursor() # creamos el cursor
        puntero.execute(crear_tabla) # utilizamos la variable crear tabla
        puntero.execute(get) # ejecutamos el 'query'
        
        try:
            # obtenemos los datos locales que necesitamos
            datos = puntero.fetchall()[-1]
            
        except Exception:
            # si no tenemos datos devolvemos 0 para manejar mejor los errores futuros
            datos = 0
            
        if datos != 0: # cuando NO es una variable en 0
        
            # verificamos que exista actualizacion de datos en la web pero sin conexion
            if hoy <= datos[-1]:
            
                # si queremos datos por consola, borramos las """ en los elementos de abajo
                """
                print("No hay actualizacion de datos")
                print(f"Valor del dolar a dia {datos[0]} es ==> {datos[1]}")
                """
                return [datos[0], datos[1]] # devolvemos los valores en una lista
                
            else:
                # llamamos a la api web ya que existe actualizacion
                # llamamos la funcion f() del script name.py que importamos y guardamos en lista
                if name.f() != 0:
                    lista = list(name.f())
                    puntero.execute(lista[-1]) # ejecutamos la variable creada en name 'insertar_datos'

                    conexion.commit() # guardar cambios locales
        
                    puntero.execute(get) 
                    datos = puntero.fetchall()[-1]
                    return [datos[0], datos[1]] # devolvemos los valores en una lista
                    
                    # si queremos tener los datos por consola para pruebas por ejemplo, quitar los """
                    """
                    print("Se han actualizado los datos!")
                    print(f"Valor del dolar a dia {datos[0]} es ==> {datos[1]}")
                    """
                    
                else:
                    return 0 # si no hay conexion a internet (o a la api) devolvemos 0
                
        else: # cuando tenemos una lista vacia (aun no obtuvimos datos de la api)
            if name.f() != 0: # si la funcion f() del script name NO regresa 0
                lista = list(name.f()) # obtenemos la lista
                puntero.execute(lista[-1]) # idem que arriba

                conexion.commit() # guardar cambios locales
                
                puntero.execute(get) # idem que arriba
                datos = puntero.fetchall()[-1] # obtenemos los datos locales que necesitamos
                return [datos[0], datos[1]] # devolvemos los valores en una lista
                
                # para imprimir en consola, sirve para pruebas, no es necesario en produccion
                """
                print("Se ha creado la base de datos y se ha actualizado!")
                print(f"Valor del dolar a dia {datos[0]} es ==> {datos[1]}")
                """
                
            else:
                return 0 # f() nos devuelve 0 y no tenemos conexion a internet (o a la api)
                
        conexion.close() # cerrar conexion local

    except Exception as e: # manejamos posible error de ejecucion
        print(f"Ocurrio el siguiente error general: {e}")

# CONTINUA EN EL PROXIMO VIDEO
