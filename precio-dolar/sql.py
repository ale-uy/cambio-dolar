import sqlite3
import name # Nuestro script anterior
import datetime


def s():
    # Variables Globales
    hoy = int(datetime.datetime.now().timestamp()) # obtenemos la fecha actual en formato unix
    # crear tabla EXCHANGES si no existe en la base de datos (BD)
    crear_tabla = "CREATE TABLE IF NOT EXISTS exchanges(last_update INTEGER NOT NULL UNIQUE, day TEXT NOT NULL, rate NUMERIC NOT NULL, next_update INTEGER NOT NULL);"
    # creamos un query para obtener datos de la BD
    get = 'SELECT day, rate, next_update FROM exchanges'

    # Trabajamos en la base de datos local
    # conexion a la base de datos; si no existe sera creada donde tenemos el script
    try:
        conexion = sqlite3.connect('storage.sqlite')
        puntero = conexion.cursor()
        puntero.execute(crear_tabla)
        puntero.execute(get)
        try:
            # obtenemos los datos locales que necesitamos
            datos = puntero.fetchall()[-1]
        except Exception:
            # si no tenemos datos devolvemos lista vacia para evitar errores
            datos = []
        if len(datos) != 0: # cuando NO es una lista vacia
            # verificamos que exista actualizacion de datos en la web pero sin conexion
            if hoy <= datos[-1]:
                pass # si queremos datos por consola, cambiamos el pass por los elementos de abajo
                # print("No hay actualizacion de datos")
                # print(f"Valor del dolar a dia {datos[0]} es ==> {datos[1]}")
            else:
                # llamamos a la api web ya que existe actualizacion
                # llamamos la funcion f() del script name que importamos y guardamos en lista
                if name.f() != 0:
                    lista = list(name.f())
                else:
                    Exception
                puntero.execute(lista[-1])
                puntero.execute(get)
                try:
                    datos = puntero.fetchall()[-1]
                    # print("Se han actualizado los datos!")
                    # print(f"Valor del dolar a dia {datos[0]} es ==> {datos[1]}")
                except Exception:
                    raise Exception
        else:
            if name.f() != 0:
                lista = list(name.f())
            else:
                Exception
            puntero.execute(lista[-1])
            puntero.execute(get)
            datos = puntero.fetchall()[-1]
            # print("Se ha creado la base de datos y se ha actualizado!")
            # print(f"Valor del dolar a dia {datos[0]} es ==> {datos[1]}")
        conexion.commit() # guardar cambios locales
        conexion.close() # cerrar conexion local
    except Exception as e:
        print(f"Ocurrio el siguiente error general: {e}")
    # obtenemos otra lista con los resultados que necesitamos mostrar luego
    return [datos[0], datos[1]]