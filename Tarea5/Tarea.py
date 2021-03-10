from Estudiante import Estudiante as est
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from R_estudiantes import *
import shelve
import re

class Registros(QMainWindow):
    def __init__(self):
        super(Registros, self).__init__() #Constructor de la clase padre
        self.ui = Ui_Registros() #se inicializa la variable ui asignando la clase que se generó en el archivo ui
        self.ui.setupUi(self) #se asigna la variable ui al mainWindow
        self.ui.registrob.setEnabled(False)
        self.ui.lecturab.setEnabled(False)
        self.ui.edicionb.setEnabled(False)
        self.ui.nombreE.textEdited.connect(self.escribirDatos)
        self.ui.correoE.textEdited.connect(self.escribirDatos)
        self.ui.contraE.textEdited.connect(self.escribirDatos)
        self.ui.registrob.clicked.connect(self.RegistroAlumno)
        self.ui.lecturab.clicked.connect(self.LecturaAlumno)
        self.ui.edicionb.clicked.connect(self.EditarAlumno)
    """
    def validarCorreo(self):
        patron1 = '(([A-Z])|([a-z])).*@{1}'  # Para asegurar que comience con letra may o min (en metodo match)
        patron2 = '\.'
        patron3 = '(?<=(@cinvestav.m))x'
        patron4 = 'mx$'
        p1 = re.match(patron1, self.ui.correoE.text())
        p2 = re.search(patron2, self.ui.correoE.text())
        p3 = re.search(patron3, self.ui.correoE.text())
        p4 = re.search(patron4, self.ui.correoE.text())
        if (p1 and p2 and p3 and p4):
            return True
        else:
            return False
    """
    """Registros.validarCorreo()"""

    def escribirDatos(self):
        if len(self.ui.nombreE.text())>1 and len(self.ui.correoE.text())>1 and len(self.ui.contraE.text())>1:
            self.ui.registrob.setEnabled(True)
            self.ui.edicionb.setEnabled(True)
        elif len(self.ui.nombreE.text())>1:
            self.ui.lecturab.setEnabled(True)

        else:
            self.ui.registrob.setEnabled(False)
            self.ui.lecturab.setEnabled(False)
            self.ui.edicionb.setEnabled(False)

    def RegistroAlumno(self):
        self.ui.lecturab.setEnabled(True)
        self.ui.edicionb.setEnabled(True)
        with shelve.open("Alumnos.db") as file:
            nombre = self.ui.nombreE.text()
            correo = self.ui.correoE.text()
            contra = self.ui.contraE.text()
            estudiante = est(nombre,correo,contra)
            file[nombre]=estudiante
        self.ui.nombreE.clear()
        self.ui.correoE.clear()
        self.ui.contraE.clear()
        self.ui.lecturab.setEnabled(False)
        self.ui.edicionb.setEnabled(False)

    def LecturaAlumno(self):
        self.ui.registrob.setEnabled(False)
        self.ui.edicionb.setEnabled(False)
        with shelve.open("Alumnos.db") as file:
            self.ui.correoE.setReadOnly(True)
            self.ui.contraE.setReadOnly(True)
            nombre = self.ui.nombreE.text()
            self.ui.nombreE.setText(nombre)
            try:
                file[nombre]
                self.ui.nombreE.setText(file[nombre].getNombre())
                self.ui.correoE.setText(file[nombre].getCorreo())
                self.ui.contraE.setText(file[nombre].getContra())
            except(KeyError):
                self.ui.nombreE.setText("Alumno no existente")
        self.ui.correoE.setReadOnly(False)
        self.ui.contraE.setReadOnly(False)
        self.ui.registrob.setEnabled(True)
        self.ui.edicionb.setEnabled(True)

    def EditarAlumno(self):
        self.ui.registrob.setEnabled(False)
        self.ui.lecturab.setEnabled(False)
        with shelve.open("Alumnos.db") as file:
            nombre = self.ui.nombreE.text()
            try:
                file[nombre]
                correo = self.ui.correoE.text()
                contra = self.ui.contraE.text()
                estudiante = est(nombre, correo, contra)
                file[nombre] = estudiante
            except(KeyError):
                self.ui.nombreE.clear()
                self.ui.correoE.clear()
                self.ui.contraE.clear()
                self.ui.nombreE.setText("Alumno no existente")
        self.ui.nombreE.clear()
        self.ui.correoE.clear()
        self.ui.contraE.clear()
        self.ui.registrob.setEnabled(True)
        self.ui.lecturab.setEnabled(True)












if __name__ == '__main__':
    # Los widgets son los elementos visuales de qt para poder mostrar los elementos visuales en qt (labels, buttons, layout,...etc.)
    import sys  # Sirve para utilizar los argumentos que se le pasen por linea de comandos

    app = QApplication(sys.argv)  # loop
    # window = QMainWindow()  # Ventana principal a utilizar en la interfaz gráfica
    window = Registros()
    window.show()  # Muestra la ventana principal gráficamente
    sys.exit((app.exec_()))  # app.exec_() valor de retorno al cerrar la aplicación
    # sys.exit muestra el valor con el que se cerro la ventana






