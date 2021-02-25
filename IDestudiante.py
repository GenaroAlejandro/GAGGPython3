class estudiante:
    __nombre = ''


    def __init__(self,nombre):
        self.__nombre=nombre



    def setDatos(self,nombre):
        self.__nombre=nombre


    def getDatos(self):
        return self.__nombre


