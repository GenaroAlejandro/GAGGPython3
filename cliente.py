from Estudiante import Estudiante as est
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from Paselista import *
import shelve
import re
import pickle
import socket


class Estudiante:
    __id = ''
    __nombre = ''
    __correo = ''
    __contra = ''

    def __init__(self, nombre, correo, contra):
        self.__nombre = nombre
        self.__correo = correo
        self.__contra = contra

    def getNombre(self):
        return self.__nombre

    def getCorreo(self):
        return self.__correo

    def getContra(self):
        return self.__contra
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
class PaseLista(QMainWindow):

    def __init__(self):
        super(PaseLista, self).__init__() #Constructor de la clase padre
        self.ui = Ui_PaseLista() #se inicializa la variable ui asignando la clase que se generó en el archivo ui
        self.ui.setupUi(self) #se asigna la variable ui al mainWindow
        self.ui.desconectarb.setEnabled(False)
        self.ui.enviarb.setEnabled(False)
        self.ui.buscarE.setEnabled(False) #Provar con setRead()
        self.ui.buscarb.setEnabled(False)
        self.ui.archivosb.setEnabled(False)
        self.ui.nombreE.setEnabled(False)
        self.ui.correoE.setEnabled(False)
        self.ui.contraE.setEnabled(False)
        self.ui.conectarb.clicked.connect(self.conexion)
        self.ui.nombreE.textEdited.connect(self.escribirDatos)
        self.ui.correoE.textEdited.connect(self.escribirDatos)
        self.ui.contraE.textEdited.connect(self.escribirDatos)
        self.ui.enviarb.clicked.connect(self.enviarDatos)
        self.ui.buscarb.clicked.connect(self.buscarArchivo)
        self.ui.buscarE.textEdited.connect(self.rutaEnviar)
        self.ui.buscarb.clicked.connect(self.enviar)
        self.ui.desconectarb.clicked.connect(self.cerrarConexion)


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

    def conexion(self):
        # host = 'localhost'
        host = '3.16.226.150'
        port = 9999
        s.connect((host, port))
        self.ui.nombreE.setEnabled(True)
        self.ui.correoE.setEnabled(True)
        self.ui.contraE.setEnabled(True)

    def escribirDatos(self):
        if len(self.ui.nombreE.text())>1 and len(self.ui.correoE.text())>1 and len(self.ui.contraE.text())>1:
            self.ui.enviarb.setEnabled(True)

        else:
            self.ui.enviarb.setEnabled(False)


    def enviarDatos(self):
        nombre = self.ui.nombreE.text()
        correo = self.ui.correoE.text()
        contra = self.ui.contraE.text()
        estudiante = Estudiante(nombre, correo, contra)
        estudiante_seriado = pickle.dumps(estudiante)
        if isinstance(estudiante,Estudiante):
            s.send(estudiante_seriado)
            res=s.recv(1024)
            res.decode()
            print(res)
        else:
            s.send(b'INI')
            res= s.recv(1024)
            print(res.decode())

            if len(estudiante_seriado)<1024:
                s.send(estudiante_seriado)

                res=s.recv(1024)
                print(res.decode())

            else:
                continuar = True
                inicio=0
                while continuar:
                    chunk=estudiante_seriado[inicio::inicio+1024]

                    if not chunk:
                        continuar = False
                        continue

                    s.send(chunk)
                    res = s.recv(1024)
                    print(res.decode())
                    inicio += 1024
            s.send(b'FIN')
            res=s.recv(1024)
            print(res.decode())

        res = s.recv(1024)
        print(f'respuesta: \n\t{res.decode()}')
        self.ui.enviarb.setEnabled(False)
        self.ui.buscarE.setEnabled(True)
        self.ui.buscarb.setEnabled(True)

    def buscarArchivo(self):
        filename, _ =QFileDialog.getOpenFileName(file='*.zip')
        self.ui.buscarE.setText(filename)
    def rutaEnviar(self):
        if self.ui.buscarE.text():
            self.ui.archivosb.setEnabled(True)

        else:
            self.ui.archivosb.setEnabled(False)
            s.send(b'INI')
            res = s.recv(1024)
            print(res.decode())

            if len(estudiante_seriado) < 1024:
                s.send(estudiante_seriado)

                res = s.recv(1024)
                print(res.decode())

            else:
                continuar = True
                inicio = 0
                while continuar:
                    chunk = estudiante_seriado[inicio::inicio + 1024]

                    if not chunk:
                        continuar = False
                        continue

                    s.send(chunk)
                    res = s.recv(1024)
                    print(res.decode())
                    inicio += 1024
            s.send(b'FIN')
            res = s.recv(1024)
            print(res.decode())

        res = s.recv(1024)


    def enviar(self):
        filename = self.ui.buscarE.text()
        file = open(filename, 'rb')
        serializado= pickle.dumps(file)
        s.send(serializado)


    def cerrarConexion (self):
        s.close()
        self.ui.desconectarb.setEnabled(False)
        self.ui.enviarb.setEnabled(True)
        self.ui.conectarb.setEnabled(False)







if __name__ == '__main__':
    # Los widgets son los elementos visuales de qt para poder mostrar los elementos visuales en qt (labels, buttons, layout,...etc.)
    import sys  # Sirve para utilizar los argumentos que se le pasen por linea de comandos

    app = QApplication(sys.argv)  # loop
    # window = QMainWindow()  # Ventana principal a utilizar en la interfaz gráfica
    window = PaseLista()
    window.show()  # Muestra la ventana principal gráficamente
    sys.exit((app.exec_()))  # app.exec_() valor de retorno al cerrar la aplicación
    # sys.exit muestra el valor con el que se cerro la ventana