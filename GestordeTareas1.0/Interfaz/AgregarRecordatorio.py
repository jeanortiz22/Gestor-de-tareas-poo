from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PyQt5.QtGui import ( QFont, QPixmap)
from PyQt5.QtWidgets import *

import icono_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1800, 880)
        MainWindow.setMaximumSize(QSize(1800, 880))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Bienvenido = QLabel(self.centralwidget)
        self.Bienvenido.setObjectName(u"Bienvenido")
        self.Bienvenido.setGeometry(QRect(380, 0, 1001, 71))
        font = QFont()
        font.setPointSize(28)
        self.Bienvenido.setFont(font)
        self.Nombredepersona = QLabel(self.centralwidget)
        self.Nombredepersona.setObjectName(u"Nombredepersona")
        self.Nombredepersona.setGeometry(QRect(380, 60, 391, 71))
        self.Nombredepersona.setFont(font)
        self.textoagregarrecordatorio = QLabel(self.centralwidget)
        self.textoagregarrecordatorio.setObjectName(u"textoagregarrecordatorio")
        self.textoagregarrecordatorio.setGeometry(QRect(200, 160, 1001, 81))
        font1 = QFont()
        font1.setPointSize(24)
        self.textoagregarrecordatorio.setFont(font1)
        self.texto_Recordatorio = QLabel(self.centralwidget)
        self.texto_Recordatorio.setObjectName(u"texto_Recordatorio")
        self.texto_Recordatorio.setGeometry(QRect(290, 290, 301, 71))
        self.texto_Recordatorio.setFont(font1)
        self.DDMMYYYY = QLineEdit(self.centralwidget)
        self.DDMMYYYY.setObjectName(u"DDMMYYYY")
        self.DDMMYYYY.setGeometry(QRect(250, 410, 1271, 51))
        font2 = QFont()
        font2.setPointSize(16)
        self.DDMMYYYY.setFont(font2)
        self.DDMMYYYY.setStyleSheet(u"QLineEdit{\n"
"	border-radius:15px;\n"
"}")
        self.HHMM = QLineEdit(self.centralwidget)
        self.HHMM.setObjectName(u"HHMM")
        self.HHMM.setGeometry(QRect(250, 510, 1271, 51))
        self.HHMM.setFont(font2)
        self.HHMM.setStyleSheet(u"QLineEdit {\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"")
        self.Botonguardar = QPushButton(self.centralwidget)
        self.Botonguardar.setObjectName(u"Botonguardar")
        self.Botonguardar.setGeometry(QRect(250, 640, 1271, 61))
        self.Botonguardar.setFont(font2)
        self.Botonguardar.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"QPushButton:Hover {\n"
"	border-bottom: 2px solid blue;\n"
"	background-color: rgb(30, 30, 30);\n"
"\n"
"}")
        self.iconocalendario = QLabel(self.centralwidget)
        self.iconocalendario.setObjectName(u"iconocalendario")
        self.iconocalendario.setGeometry(QRect(120, 170, 61, 61))
        self.iconocalendario.setPixmap(QPixmap(u":/icono/calendario.png"))
        self.iconocalendario.setScaledContents(True)
        self.iconolibro = QLabel(self.centralwidget)
        self.iconolibro.setObjectName(u"iconolibro")
        self.iconolibro.setGeometry(QRect(280, 20, 81, 71))
        self.iconolibro.setPixmap(QPixmap(u":/icono/libro-abierto.png"))
        self.iconolibro.setScaledContents(True)
        self.iconocampana = QLabel(self.centralwidget)
        self.iconocampana.setObjectName(u"iconocampana")
        self.iconocampana.setGeometry(QRect(200, 280, 71, 71))
        self.iconocampana.setPixmap(QPixmap(u":/icono/campana.png"))
        self.iconocampana.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Bienvenido.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a tu gestor de tareas ", None))
        self.Nombredepersona.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.textoagregarrecordatorio.setText(QCoreApplication.translate("MainWindow", u"Agregar Recordatorio", None))
        self.texto_Recordatorio.setText(QCoreApplication.translate("MainWindow", u"Recordatorio", None))
        self.DDMMYYYY.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.HHMM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
#if QT_CONFIG(whatsthis)
        self.Botonguardar.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guardar</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Botonguardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.iconocalendario.setText("")
        self.iconolibro.setText("")
        self.iconocampana.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarRecordatorio_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(AgregarRecordatorio_MainWindow)
    AgregarRecordatorio_MainWindow.show()
    sys.exit(app.exec_())
