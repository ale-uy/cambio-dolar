
# Creamos el archivo name.py

# Usaremos la API currency de https://open.exchangerate-api.com/v6/latest

from datetime import datetime # paquete que usaremos

# Paquete a instalar con pip
import requests


def f():
    # url de la api
    url = 'https://open.exchangerate-api.com/v6/latest'

    # obtener datos en formato json si es posible
    try:
        response = requests.get(url)
        data = response.json()

        # elegir moneda de interes del json de ejemplo dentro de 'rates' (api_ejemplo.json)
        moneda = 'UYU'
        
        # iteramos los datos CLAVE (keys) del json para obtener los valores como 'time_last_update_unix' (diccionario)
        for i in data.keys():
            if i == 'time_last_update_unix':
                next_update = int(data['time_next_update_unix']) # guardamos fecha siguiente actualizacion
                last_update = int(data['time_last_update_unix']) # y fecha ultima actualizacion

                # lista de meses para usar datos unix en formato legible
                meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre']
                aux = datetime.utcfromtimestamp(last_update) # variable con fecha en unix

                # imprimimos la fecha en formato '27 de Mayo del 2020'
                day = str(f'{aux.day} de {meses[aux.month-1]} del {aux.year}')

            elif i == 'rates':
                # obtengo el valor del dolar en la moneda elegida
                rate = float(data[i][moneda])

            else: # no es necesario esta parte, no hace nada en realidad pero queda bien un else
                continue

        # la usaremos a futuro para insertar datos
        insertar_datos = f"INSERT INTO exchanges(last_update, day, rate, next_update) VALUES ({last_update}, '{day}', {rate}, {next_update})"

        # devolvemos los resultados en una lista
        return [last_update, day, rate, next_update, insertar_datos]

    # devolvemos error si no hay conexion
    except Exception:
        print("Server not found") # para usarlo en el debug
        return 0 # lo usaremos para facilitar las proximas tareas

# CONTINUA EN EL PROXIMO VIDEO
