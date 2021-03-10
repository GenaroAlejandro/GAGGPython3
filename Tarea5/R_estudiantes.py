# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'R_estudiantes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Registros(object):
    def setupUi(self, Registros):
        if not Registros.objectName():
            Registros.setObjectName(u"Registros")
        Registros.resize(352, 222)
        self.contraE = QLineEdit(Registros)
        self.contraE.setObjectName(u"contraE")
        self.contraE.setGeometry(QRect(111, 72, 133, 20))
        self.nombreE = QLineEdit(Registros)
        self.nombreE.setObjectName(u"nombreE")
        self.nombreE.setGeometry(QRect(111, 20, 133, 20))
        self.correoE = QLineEdit(Registros)
        self.correoE.setObjectName(u"correoE")
        self.correoE.setGeometry(QRect(111, 46, 133, 20))
        self.nombrel = QLabel(Registros)
        self.nombrel.setObjectName(u"nombrel")
        self.nombrel.setGeometry(QRect(49, 20, 37, 16))
        self.correol = QLabel(Registros)
        self.correol.setObjectName(u"correol")
        self.correol.setGeometry(QRect(49, 46, 33, 16))
        self.contral = QLabel(Registros)
        self.contral.setObjectName(u"contral")
        self.contral.setGeometry(QRect(49, 72, 56, 16))
        self.edicionb = QPushButton(Registros)
        self.edicionb.setObjectName(u"edicionb")
        self.edicionb.setGeometry(QRect(201, 100, 75, 23))
        self.registrob = QPushButton(Registros)
        self.registrob.setObjectName(u"registrob")
        self.registrob.setGeometry(QRect(39, 100, 75, 23))
        self.lecturab = QPushButton(Registros)
        self.lecturab.setObjectName(u"lecturab")
        self.lecturab.setGeometry(QRect(120, 100, 75, 23))

        self.retranslateUi(Registros)

        QMetaObject.connectSlotsByName(Registros)
    # setupUi

    def retranslateUi(self, Registros):
        Registros.setWindowTitle(QCoreApplication.translate("Registros", u"Registros", None))
        self.nombrel.setText(QCoreApplication.translate("Registros", u"Nombre", None))
        self.correol.setText(QCoreApplication.translate("Registros", u"Correo", None))
        self.contral.setText(QCoreApplication.translate("Registros", u"Contrase\u00f1a", None))
        self.edicionb.setText(QCoreApplication.translate("Registros", u"Edici\u00f3n", None))
        self.registrob.setText(QCoreApplication.translate("Registros", u"Registro", None))
        self.lecturab.setText(QCoreApplication.translate("Registros", u"Lectura", None))
    # retranslateUi

