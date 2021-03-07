import numpy as np
from mongoengine import *
from datetime import datetime

class estudiante():
    __nombre = ''
    __correo = ''
    __contraseña = ''
    __materias = ''


    def __init__(self,nombre,correo,contraseña,materias):
        self.__nombre=nombre
        self.__correo = correo
        self.__contraseña = contraseña
        self.__materias = materias

    def setDatos(self,nombre,correo,contraseña,materias):
        self.__nombre=nombre
        self.__correo=correo
        self.__contraseña=contraseña
        self.__materias=materias


    def getDatos(self):
        return self.__nombre, self.__correo, self.__contraseña,self.__materias


