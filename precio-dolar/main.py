
# Creamos el archivo main.py
# En este archivo haremos la conexion a la ui y la pondremos en pantalla

# paquetes a importar
import sys
import sql # nuestro script anterior

# necesitamos instalar pyside2 (pip install pyside2)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile


# El siguiente codigo es parte de la libreria PySide2
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # obtenemos la gui que diseñamos con nombre 'design.ui' (debe estar en la misma carpeta que este script)
    ui_file_name = "design.ui" # si cambiamos el nombre debemos cambiarlo por el que le pusimos

    ui_file = QFile(ui_file_name) # indicamos el archivo ui a usar
    loader = QUiLoader() # carga el archivo
    window = loader.load(ui_file) # ahora tenemos la gui en la clase 'window' para poder editarla

    # Aqui va nuestro codigo para editar la ui
    
    datos = sql.s() # obtenemos la lista desde sql.py

    if datos != 0: # si no tuvimos errores en etapas anteriores
        window.lcdNumber.display(datos[1]) # mostramos el valor de cambio en el lcd
        window.label.setText(f"{datos[0]}") # mostramos la fecha en el label
        
    else: # si tuvimos algun error en ejecucion anterior
        window.lcdNumber.display("Error")
        window.label.setText("Error al conectar")

    ui_file.close() # cerramos la edicion

    # lo usa pyside2 para control de errores si no puede cargar la ui
    if not window: 
        print(loader.errorString())
        sys.exit(-1)

    window.show() # muestra la pantalla
    sys.exit(app.exec_()) # y la mantiene activa

# FIN
