import sys
import sql

# necesitamos instalar pyside2 (pip install pyside2)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile


# El siguiente codigo sin comentar es parte de la libreria
if __name__ == "__main__":

    app = QApplication(sys.argv)

    # obtenemos la gui que diseñamos con nombre 'design.ui', cambiar nombre si usamos otro
    ui_file_name = "design.ui"

    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file) # ahora tenemos la gui en la clase 'window' para poder editarla

    datos = sql.s() # obtenemos la lista desde sql.py
    window.lcdNumber.display(datos[1]) # mostramos el valor de cambio en el lcd
    window.label.setText(f"{datos[0]}") # mostramos la fecha en el label

    ui_file.close() # cerramos la edicion

    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    sys.exit(app.exec_())