import sys, os
# Класс QUrl предоставляет удобный интерфейс для работы с Urls
from PyQt5.QtCore import pyqtProperty, pyqtSignal, QCoreApplication, QObject, QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QWidget
# Класс QQuickView предоставляет возможность отображать QML файлы.
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

class Dash(QObject):
    dash_update = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._speed = 12
        self.timer=QTimer()
        self.timer.timeout.connect(self.new_values)
        self.timer.start(100)

    def new_values(self):
        if self._speed >= 50:
            self.timer.stop()
        else:
            self._speed = self._speed + 1
            self.dash_update.emit()

    # Define the getter of the 'name' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty(int, notify=dash_update)
    def speed(self):
        return self._speed

    # Define the setter of the 'name' property.
    #speed.setter
    #def speed(self, speed):
        #self._speed = speed

if __name__ == '__main__':

    #os.chdir('/home/user/opt/Qt/Tools/QtDesignStudio/share/qtcreator/examples/ClusterTutorial/')
    #os.environ["QML2_IMPORT_PATH"] = "/home/user/opt/Qt/Tools/QtDesignStudio/share/qtcreator/examples/ClusterTutorial/"
    app = QApplication(sys.argv)
    # Объект QQuickView, в который грузится UI для отображения
    view = QQuickView()
    qmlRegisterType(Dash, 'Dash', 1, 0, 'Dash')
    #view.addImportPath(QUrl('/home/user/opt/Qt/Tools/QtDesignStudio/share/qtcreator/examples/ClusterTutorial/'))
    #view.setSource(QUrl('/home/user/opt/Qt/Tools/QtDesignStudio/share/qtcreator/examples/ClusterTutorial/ClusterTutorial.qml'))
    view.setSource(QUrl('./test.qml'))
    view.show()
    app.exec_()
    sys.exit()
