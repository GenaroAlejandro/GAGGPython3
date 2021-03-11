# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Paselista.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PaseLista(object):
    def setupUi(self, PaseLista):
        if not PaseLista.objectName():
            PaseLista.setObjectName(u"PaseLista")
        PaseLista.resize(665, 571)
        self.archivol = QLabel(PaseLista)
        self.archivol.setObjectName(u"archivol")
        self.archivol.setGeometry(QRect(138, 230, 66, 16))
        self.correol = QLabel(PaseLista)
        self.correol.setObjectName(u"correol")
        self.correol.setGeometry(QRect(57, 149, 33, 16))
        self.nombreE = QLineEdit(PaseLista)
        self.nombreE.setObjectName(u"nombreE")
        self.nombreE.setGeometry(QRect(138, 123, 133, 20))
        self.informacionl = QLabel(PaseLista)
        self.informacionl.setObjectName(u"informacionl")
        self.informacionl.setGeometry(QRect(138, 104, 111, 16))
        self.enviarb = QPushButton(PaseLista)
        self.enviarb.setObjectName(u"enviarb")
        self.enviarb.setGeometry(QRect(138, 201, 96, 23))
        self.buscarE = QLineEdit(PaseLista)
        self.buscarE.setObjectName(u"buscarE")
        self.buscarE.setGeometry(QRect(138, 249, 133, 20))
        self.correoE = QLineEdit(PaseLista)
        self.correoE.setObjectName(u"correoE")
        self.correoE.setGeometry(QRect(138, 149, 133, 20))
        self.contraE = QLineEdit(PaseLista)
        self.contraE.setObjectName(u"contraE")
        self.contraE.setGeometry(QRect(138, 175, 133, 20))
        self.archivosb = QPushButton(PaseLista)
        self.archivosb.setObjectName(u"archivosb")
        self.archivosb.setGeometry(QRect(138, 278, 81, 23))
        self.nombrel = QLabel(PaseLista)
        self.nombrel.setObjectName(u"nombrel")
        self.nombrel.setGeometry(QRect(57, 123, 37, 16))
        self.buscarb = QPushButton(PaseLista)
        self.buscarb.setObjectName(u"buscarb")
        self.buscarb.setGeometry(QRect(57, 249, 75, 23))
        self.contral = QLabel(PaseLista)
        self.contral.setObjectName(u"contral")
        self.contral.setGeometry(QRect(57, 175, 56, 16))
        self.label = QLabel(PaseLista)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(49, 37, 111, 21))
        self.desconectarb = QPushButton(PaseLista)
        self.desconectarb.setObjectName(u"desconectarb")
        self.desconectarb.setGeometry(QRect(173, 70, 91, 21))
        self.conectarb = QPushButton(PaseLista)
        self.conectarb.setObjectName(u"conectarb")
        self.conectarb.setGeometry(QRect(50, 70, 91, 21))

        self.retranslateUi(PaseLista)

        QMetaObject.connectSlotsByName(PaseLista)
    # setupUi

    def retranslateUi(self, PaseLista):
        PaseLista.setWindowTitle(QCoreApplication.translate("PaseLista", u"Datos", None))
        self.archivol.setText(QCoreApplication.translate("PaseLista", u"          Archivo", None))
        self.correol.setText(QCoreApplication.translate("PaseLista", u"Correo", None))
        self.informacionl.setText(QCoreApplication.translate("PaseLista", u"Informacion Estudiante", None))
        self.enviarb.setText(QCoreApplication.translate("PaseLista", u"Enviar informacion", None))
        self.archivosb.setText(QCoreApplication.translate("PaseLista", u"Enviar archivos", None))
        self.nombrel.setText(QCoreApplication.translate("PaseLista", u"Nombre", None))
        self.buscarb.setText(QCoreApplication.translate("PaseLista", u"Buscar", None))
        self.contral.setText(QCoreApplication.translate("PaseLista", u"Contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("PaseLista", u"Conexi\u00f3n con servidor", None))
        self.desconectarb.setText(QCoreApplication.translate("PaseLista", u"Desconectar", None))
        self.conectarb.setText(QCoreApplication.translate("PaseLista", u"Conectar", None))
    # retranslateUi

