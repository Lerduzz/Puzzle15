# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaJuego(object):
    def setupUi(self, VentanaJuego):
        VentanaJuego.setObjectName("VentanaJuego")
        VentanaJuego.resize(499, 540)
        VentanaJuego.setMinimumSize(QtCore.QSize(499, 540))
        VentanaJuego.setMaximumSize(QtCore.QSize(499, 540))
        VentanaJuego.setStyleSheet("QWidget {\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #646464;\n"
"    color: #ff2424;\n"
"}\n"
"\n"
"QStatusBar, QMenuBar {\n"
"    background-color: #121212;\n"
"    color: #1212ff;\n"
"}")
        self.Tablero = QtWidgets.QWidget(VentanaJuego)
        self.Tablero.setObjectName("Tablero")
        self.gridLayout = QtWidgets.QGridLayout(self.Tablero)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.boton08 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton08.sizePolicy().hasHeightForWidth())
        self.boton08.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton08.setFont(font)
        self.boton08.setObjectName("boton08")
        self.gridLayout.addWidget(self.boton08, 1, 3, 1, 1)
        self.boton12 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton12.sizePolicy().hasHeightForWidth())
        self.boton12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton12.setFont(font)
        self.boton12.setObjectName("boton12")
        self.gridLayout.addWidget(self.boton12, 2, 3, 1, 1)
        self.boton06 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton06.sizePolicy().hasHeightForWidth())
        self.boton06.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton06.setFont(font)
        self.boton06.setObjectName("boton06")
        self.gridLayout.addWidget(self.boton06, 1, 1, 1, 1)
        self.boton07 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton07.sizePolicy().hasHeightForWidth())
        self.boton07.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton07.setFont(font)
        self.boton07.setObjectName("boton07")
        self.gridLayout.addWidget(self.boton07, 1, 2, 1, 1)
        self.boton02 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton02.sizePolicy().hasHeightForWidth())
        self.boton02.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton02.setFont(font)
        self.boton02.setObjectName("boton02")
        self.gridLayout.addWidget(self.boton02, 0, 1, 1, 1)
        self.boton05 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton05.sizePolicy().hasHeightForWidth())
        self.boton05.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton05.setFont(font)
        self.boton05.setObjectName("boton05")
        self.gridLayout.addWidget(self.boton05, 1, 0, 1, 1)
        self.boton09 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton09.sizePolicy().hasHeightForWidth())
        self.boton09.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton09.setFont(font)
        self.boton09.setObjectName("boton09")
        self.gridLayout.addWidget(self.boton09, 2, 0, 1, 1)
        self.boton03 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton03.sizePolicy().hasHeightForWidth())
        self.boton03.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton03.setFont(font)
        self.boton03.setObjectName("boton03")
        self.gridLayout.addWidget(self.boton03, 0, 2, 1, 1)
        self.boton11 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton11.sizePolicy().hasHeightForWidth())
        self.boton11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton11.setFont(font)
        self.boton11.setObjectName("boton11")
        self.gridLayout.addWidget(self.boton11, 2, 2, 1, 1)
        self.boton01 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton01.sizePolicy().hasHeightForWidth())
        self.boton01.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton01.setFont(font)
        self.boton01.setObjectName("boton01")
        self.gridLayout.addWidget(self.boton01, 0, 0, 1, 1)
        self.boton04 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton04.sizePolicy().hasHeightForWidth())
        self.boton04.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton04.setFont(font)
        self.boton04.setObjectName("boton04")
        self.gridLayout.addWidget(self.boton04, 0, 3, 1, 1)
        self.boton10 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton10.sizePolicy().hasHeightForWidth())
        self.boton10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton10.setFont(font)
        self.boton10.setObjectName("boton10")
        self.gridLayout.addWidget(self.boton10, 2, 1, 1, 1)
        self.boton13 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton13.sizePolicy().hasHeightForWidth())
        self.boton13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton13.setFont(font)
        self.boton13.setObjectName("boton13")
        self.gridLayout.addWidget(self.boton13, 3, 0, 1, 1)
        self.boton14 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton14.sizePolicy().hasHeightForWidth())
        self.boton14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton14.setFont(font)
        self.boton14.setObjectName("boton14")
        self.gridLayout.addWidget(self.boton14, 3, 1, 1, 1)
        self.boton15 = QtWidgets.QPushButton(self.Tablero)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton15.sizePolicy().hasHeightForWidth())
        self.boton15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boton15.setFont(font)
        self.boton15.setObjectName("boton15")
        self.gridLayout.addWidget(self.boton15, 3, 2, 1, 1)
        VentanaJuego.setCentralWidget(self.Tablero)
        self.menubar = QtWidgets.QMenuBar(VentanaJuego)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        self.menuJuego = QtWidgets.QMenu(self.menubar)
        self.menuJuego.setObjectName("menuJuego")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        VentanaJuego.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaJuego)
        self.statusbar.setObjectName("statusbar")
        VentanaJuego.setStatusBar(self.statusbar)
        self.actionDesordenar = QtWidgets.QAction(VentanaJuego)
        self.actionDesordenar.setObjectName("actionDesordenar")
        self.actionOrdenar = QtWidgets.QAction(VentanaJuego)
        self.actionOrdenar.setObjectName("actionOrdenar")
        self.actionSalir = QtWidgets.QAction(VentanaJuego)
        self.actionSalir.setObjectName("actionSalir")
        self.actionInstrucciones = QtWidgets.QAction(VentanaJuego)
        self.actionInstrucciones.setObjectName("actionInstrucciones")
        self.actionCreditos = QtWidgets.QAction(VentanaJuego)
        self.actionCreditos.setObjectName("actionCreditos")
        self.menuJuego.addAction(self.actionDesordenar)
        self.menuJuego.addAction(self.actionOrdenar)
        self.menuJuego.addSeparator()
        self.menuJuego.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionInstrucciones)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionCreditos)
        self.menubar.addAction(self.menuJuego.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(VentanaJuego)
        QtCore.QMetaObject.connectSlotsByName(VentanaJuego)

    def retranslateUi(self, VentanaJuego):
        _translate = QtCore.QCoreApplication.translate
        VentanaJuego.setWindowTitle(_translate("VentanaJuego", "Puzzle en Python"))
        self.boton08.setText(_translate("VentanaJuego", "8"))
        self.boton12.setText(_translate("VentanaJuego", "12"))
        self.boton06.setText(_translate("VentanaJuego", "6"))
        self.boton07.setText(_translate("VentanaJuego", "7"))
        self.boton02.setText(_translate("VentanaJuego", "2"))
        self.boton05.setText(_translate("VentanaJuego", "5"))
        self.boton09.setText(_translate("VentanaJuego", "9"))
        self.boton03.setText(_translate("VentanaJuego", "3"))
        self.boton11.setText(_translate("VentanaJuego", "11"))
        self.boton01.setText(_translate("VentanaJuego", "1"))
        self.boton04.setText(_translate("VentanaJuego", "4"))
        self.boton10.setText(_translate("VentanaJuego", "10"))
        self.boton13.setText(_translate("VentanaJuego", "13"))
        self.boton14.setText(_translate("VentanaJuego", "14"))
        self.boton15.setText(_translate("VentanaJuego", "15"))
        self.menuJuego.setTitle(_translate("VentanaJuego", "Juego"))
        self.menuAyuda.setTitle(_translate("VentanaJuego", "Ayuda"))
        self.actionDesordenar.setText(_translate("VentanaJuego", "Desordenar"))
        self.actionOrdenar.setText(_translate("VentanaJuego", "Ordenar"))
        self.actionSalir.setText(_translate("VentanaJuego", "Salir"))
        self.actionInstrucciones.setText(_translate("VentanaJuego", "Instrucciones"))
        self.actionCreditos.setText(_translate("VentanaJuego", "Creditos"))
