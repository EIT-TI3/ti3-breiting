from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPolygonF
from PyQt5.QtCore import QPointF, QTimer

import sys, math
from koordinate import Kabinett, Koord3D
from location import LocationAt


class BBoardWidget(QWidget):
    def __init__(self, xmax=50, ymax=50, scale=1.0):
        super().__init__()
        self.__xmax = abs(xmax)
        self.__ymax = abs(ymax)
        self.__scale = abs(scale)
        self.__shape = []
        self.setMinimumSize(200, 200)
        self.resize(450, 350)
        self.setWindowTitle("Breadboard Replay")

    def setShape(self, polygon_array):
        self.__shape = tuple(polygon_array)  # uebertrage das neue Shape in das Attribut
        self.update()  # zeichne das Widget neu

    # ueberschreibe die Standard-paintEvent-Routine
    def paintEvent(self, e):
        super().paintEvent(e)
        # size=e.rect()
        # (width, height)=(size.width(), size.height())
        qp = QPainter()
        qp.begin(self)
        qp.setWindow(-self.__xmax, -self.__ymax, 2 * self.__xmax, 2 * self.__ymax)
        qp.scale(self.__scale, -self.__scale)
        for p in self.__shape:
            qpoints = [QPointF(i.x, i.y) for i in p]
            qp.drawPolygon(QPolygonF(qpoints))
        qp.end()


# Eigene Timer-Klasse, die alle 250 ms ein Ereignis auslöst
# und ein neues Shape an das BBWidget schickt
class MyTimer(QTimer):
    __TimerInc = 250

    def __init__(self, bbwidget_, loc_, shape_):
        super().__init__(bbwidget_)
        self.__timerValue = 0
        self.__bbwidget = bbwidget_
        self.__location = loc_
        self.__shape = shape_

        self.timeout.connect(self.__callback)  # rufe alle 250 ms die callback-Methode auf

    # callback-Methode, die alle MyTimer.__timerInc [ms] das Standard-Shape rotiert,
    # um die Lage zu aktualisieren und es dann zu zeichnen
    def __callback(self):
        if self.__timerValue <= self.__location.last_timestamp():  # existiert der Zeitwert noch in der CSV-Datei
            z_angle = self.__location.get_nick(self.__timerValue)
            x_angle = self.__location.get_roll(self.__timerValue)

            # gib den aktuellen Zeitwert auf der Konsole aus
            print('timerval: {} -> x={:.2f} z={:.2f}'.format(self.__timerValue,
                                                             x_angle * 180 / math.pi,
                                                             z_angle * 180 / math.pi))

            rot_shape = [[point.rotate_x(x_angle) for point in polygon] for polygon in self.__shape]
            rot_shape = [[Kabinett(point.rotate_z(z_angle)) for point in polygon] for polygon in rot_shape]

            # gib das rotierte Shape aus
            self.__bbwidget.setShape(rot_shape)
            # erhoehe Zeitwert um das Intervall
            self.__timerValue += MyTimer.__TimerInc
        # Zeitwert nicht mehr vorhanden -> Timer stoppen
        else:
            self.stop()
            self.__timerValue = 0

    # Ueberschriebene Methode, um den Timer zu starten
    def start(self, **kwargs):
        return super().start(MyTimer.__TimerInc)


# Hauptprogramm
if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    bbwidget = BBoardWidget()
    location = LocationAt('xRotFirst.csv' if len(sys.argv) < 2 else sys.argv[1])

    # Definiere Breadboard-Shape
    shape = [[Koord3D(-18, -3, -5), Koord3D(18, -3, -5), Koord3D(18, -3, 5), Koord3D(-18, -3, 5)],  # untere Flaeche
             [Koord3D(-18, 3, -5), Koord3D(18, 3, -5), Koord3D(18, 3, 5), Koord3D(-18, 3, 5)],  # obere Flaeche
             [Koord3D(-18, -3, -5), Koord3D(-18, 3, -5), Koord3D(-18, 3, 5), Koord3D(-18, -3, 5)],  # hintere Flaeche
             [Koord3D(18, -3, -5), Koord3D(18, 3, -5), Koord3D(18, -3, 5), Koord3D(18, 3, 5)]  # vordere Flaeche
             ]

    bbwidget.show()

    timer = MyTimer(bbwidget, location, shape)
    timer.start()

    qapp.exec()
