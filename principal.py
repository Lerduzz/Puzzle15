from PyQt5 import QtWidgets
from ventana import Ui_VentanaJuego
import sys, random

MARGEN = 5
SEPARACION = 3

class VentanaJuego(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaJuego, self).__init__()
        self.ui = Ui_VentanaJuego() 
        self.ui.setupUi(self)

        self.estaDesordenado = False
        self.cantidadMovimientos = 0

        self.ui.actionSalir.triggered.connect(self.accionSalir)
        self.ui.actionDesordenar.triggered.connect(self.desordenar)
        self.ui.actionOrdenar.triggered.connect(self.ordenar)
        self.ui.actionInstrucciones.triggered.connect(self.ayuda)
        self.ui.actionCreditos.triggered.connect(self.creditos)

        self.botones = [
            self.ui.boton01,
            self.ui.boton02,
            self.ui.boton03,
            self.ui.boton04,
            self.ui.boton05,
            self.ui.boton06,
            self.ui.boton07,
            self.ui.boton08,
            self.ui.boton09,
            self.ui.boton10,
            self.ui.boton11,
            self.ui.boton12,
            self.ui.boton13,
            self.ui.boton14,
            self.ui.boton15
        ]

        self.acciones = [
            self.botonClick01,
            self.botonClick02,
            self.botonClick03,
            self.botonClick04,
            self.botonClick05,
            self.botonClick06,
            self.botonClick07,
            self.botonClick08,
            self.botonClick09,
            self.botonClick10,
            self.botonClick11,
            self.botonClick12,
            self.botonClick13,
            self.botonClick14,
            self.botonClick15,
        ]

        for i in range(15):
            self.botones[i].clicked.connect(self.acciones[i])

    def accionSalir(self):
        sys.exit(0)

    def ayuda(self):
        # self.ui.statusbar.showMessage('Mueve las casillas al espacio vacio y ordena el tablero.', 60000)
        QtWidgets.QMessageBox.information(
            self,
            'Ayuda',
            'Mueve las casillas al espacio vacio hasta ordenar el tablero.',
        )

    def creditos(self):
        # self.ui.statusbar.showMessage('Desarrollado por Lerduzz (https://youtube.com/@lerduzz).', 60000)
        QtWidgets.QMessageBox.information(
            self,
            'Creditos',
            'Desarrollado por Lerduzz\n\nhttps://youtube.com/@lerduzz',
        )

    def botonClick01(self):
        self.comprobarClick(0)

    def botonClick02(self):
        self.comprobarClick(1)

    def botonClick03(self):
        self.comprobarClick(2)

    def botonClick04(self):
        self.comprobarClick(3)

    def botonClick05(self):
        self.comprobarClick(4)

    def botonClick06(self):
        self.comprobarClick(5)

    def botonClick07(self):
        self.comprobarClick(6)

    def botonClick08(self):
        self.comprobarClick(7)

    def botonClick09(self):
        self.comprobarClick(8)

    def botonClick10(self):
        self.comprobarClick(9)

    def botonClick11(self):
        self.comprobarClick(10)

    def botonClick12(self):
        self.comprobarClick(11)

    def botonClick13(self):
        self.comprobarClick(12)

    def botonClick14(self):
        self.comprobarClick(13)

    def botonClick15(self):
        self.comprobarClick(14)

    def comprobarClick(self, indice):
        if self.estaDesordenado:
            if self.comprobarMovimiento(indice):
                self.cantidadMovimientos += 1
                if self.estaOrdenado():
                    self.estaDesordenado = False
                    self.ui.statusbar.showMessage('¡Felicitaciones! Has ganado en ' + str(self.cantidadMovimientos) + ' movimientos.', 10000)
                    QtWidgets.QMessageBox.information(
                        self,
                        'Has ganado',
                        '¡Felicitaciones!\n\nHas ganado en ' + str(self.cantidadMovimientos) + ' movimientos.',
                    )
                else:
                    self.ui.statusbar.showMessage('Actualmente has realizado ' + str(self.cantidadMovimientos) + ' movimientos.', 2500)
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    'Advertencia',
                    '¡Solo puedes mover las casillas que se encuentran al lado del espacio vacio!',
                )
        else:
            # self.ui.statusbar.showMessage('¡Primero debes desordenar el tablero para poder jugar!', 10000)
            QtWidgets.QMessageBox.critical(
                self,
                'Error',
                '¡Primero debes desordenar el tablero para poder jugar!\n\nHas clic en el menú \'Juego\' y luego en \'Desordenar\'.',
            )

    def comprobarMovimiento(self, indice):
        boton = self.botones[indice]
        x = boton.x()
        y = boton.y()
        ancho = boton.width()
        alto = boton.height()
        if self.vacioLeft(x, y, ancho, alto):
            self.moverLeft(indice)
            return True
        elif self.vacioRight(x, y, ancho, alto):
            self.moverRight(indice)
            return True
        elif self.vacioUp(x, y, ancho, alto):
            self.moverUp(indice)
            return True
        elif self.vacioDown(x, y, ancho, alto):
            self.moverDown(indice)
            return True
        return False

    def vacioLeft(self, x, y, ancho, alto):
        if x == MARGEN:
            return False
        for b in self.botones:
            if b.x() == x - SEPARACION - ancho and b.y() == y:
                return False
        return True

    def vacioRight(self, x, y, ancho, alto):
        if x == MARGEN + SEPARACION * 3 + ancho * 3:
            return False
        for b in self.botones:
            if b.x() == x + SEPARACION + ancho and b.y() == y:
                return False
        return True

    def vacioUp(self, x, y, ancho, alto):
        if y == MARGEN:
            return False
        for b in self.botones:
            if b.y() == y - SEPARACION - alto and b.x() == x:
                return False
        return True

    def vacioDown(self, x, y, ancho, alto):
        if y == MARGEN + SEPARACION * 3 + alto * 3:
            return False
        for b in self.botones:
            if b.y() == y + SEPARACION + alto and b.x() == x:
                return False
        return True

    def moverLeft(self, indice):
        boton = self.botones[indice]
        boton.move(boton.x() - boton.width() - SEPARACION, boton.y())

    def moverRight(self, indice):
        boton = self.botones[indice]
        boton.move(boton.x() + boton.width() + SEPARACION, boton.y())

    def moverUp(self, indice):
        boton = self.botones[indice]
        boton.move(boton.x(), boton.y() - boton.height() - SEPARACION)

    def moverDown(self, indice):
        boton = self.botones[indice]
        boton.move(boton.x(), boton.y() + boton.height() + SEPARACION)

    def desordenar(self):
        movimientos = 1000
        while movimientos > 0:
            rnd = random.randint(0, 14)
            if self.comprobarMovimiento(rnd):
                movimientos -= 1
        self.estaDesordenado = True
        self.cantidadMovimientos = 0

    def ordenar(self):
        for i in range(15):
            boton = self.botones[i]
            ancho = boton.width()
            alto = boton.height()
            dx = int(i % 4)
            dy = int(i / 4)
            x = boton.x()
            y = boton.y()
            ox = MARGEN + dx * ancho + dx * SEPARACION 
            oy = MARGEN + dy * alto + dy * SEPARACION
            if x != ox or y != oy:
                boton.move(ox, oy)
        self.estaDesordenado = False

    def estaOrdenado(self):
        for i in range(15):
            boton = self.botones[i]
            ancho = boton.width()
            alto = boton.height()
            dx = int(i % 4)
            dy = int(i / 4)
            x = boton.x()
            y = boton.y()
            ox = MARGEN + dx * ancho + dx * SEPARACION 
            oy = MARGEN + dy * alto + dy * SEPARACION
            if x != ox or y != oy:
                return False
        return True

app = QtWidgets.QApplication([])
application = VentanaJuego()
application.show()
sys.exit(app.exec())