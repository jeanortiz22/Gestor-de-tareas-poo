from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QMetaObject,QRect, QSize,QDateTime)
from PyQt5.QtGui import ( QFont, QPixmap, QColor)
from PyQt5.QtWidgets import *
from Calendario1 import Ui_CalendarioDialog

import icono_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1001, 625)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textoagregarrecordatorio = QLabel(self.centralwidget)
        self.textoagregarrecordatorio.setObjectName(u"textoagregarrecordatorio")
        self.textoagregarrecordatorio.setGeometry(QRect(160, 40, 10000, 80))
        font = QFont()
        font.setPointSize(20)
        self.textoagregarrecordatorio.setFont(font)
        self.texto_Recordatorio = QLabel(self.centralwidget)
        self.texto_Recordatorio.setObjectName(u"texto_Recordatorio")
        self.texto_Recordatorio.setGeometry(QRect(170, 180, 301, 71))
        self.texto_Recordatorio.setFont(font)
        self.fecha = QDateTimeEdit(self.centralwidget)
        self.fecha.setObjectName("fecha")
        self.fecha.setGeometry(QRect(110, 290, 791, 51))
        self.fecha.setDisplayFormat("dd/MM/yyyy HH:mm")  # Formato de fecha y hora
        font1 = QFont()
        font1.setPointSize(16)
        self.fecha.setFont(font1)
        self.fecha.setStyleSheet("border-radius:15px;")

        self.fecha.setDateTime(QDateTime.currentDateTime())  # Establecer la fecha y hora actuales como valor inicial
        self.fecha.setButtonSymbols(QAbstractSpinBox.NoButtons) # Eliminar los botones de incremento y decremento

        # Crear botón de calendario
        self.botonCalendario = QPushButton(self.centralwidget)
        self.botonCalendario.setObjectName(u"botonCalendario")
        self.botonCalendario.setText("📅")
        self.botonCalendario.setGeometry(QRect(900, 290, 51, 51))  # Posicionamiento del botón
        self.botonCalendario.clicked.connect(self.abrirCalendario)  # Conectar el botón al metodo abrirCalendario


        self.Botonguardar = QPushButton(self.centralwidget)
        self.Botonguardar.setObjectName(u"Botonguardar")
        self.Botonguardar.setGeometry(QRect(110, 420, 791, 61))
        self.Botonguardar.setFont(font1)
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
        self.iconocalendario.setGeometry(QRect(80, 50, 61, 61))
        self.iconocalendario.setPixmap(QPixmap(u":/icono/calendario.png"))
        self.iconocalendario.setScaledContents(True)
        self.iconocampana = QLabel(self.centralwidget)
        self.iconocampana.setObjectName(u"iconocampana")
        self.iconocampana.setGeometry(QRect(110, 190, 51, 51))
        self.iconocampana.setPixmap(QPixmap(u":/icono/campana.png"))
        self.iconocampana.setScaledContents(True)
        self.recordatorioError = QLabel(self.centralwidget)
        self.recordatorioError.setObjectName(u"label")
        self.recordatorioError.setGeometry(QRect(120, 355, 771, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.recordatorioError.setFont(font2)
        self.recordatorioError.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 0, 4);\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    # Metodo para abrir el calendario
    def abrirCalendario(self):
        self.calendario_dialog = QtWidgets.QDialog()  # Crear el diálogo para el calendario
        self.ui_calendario = Ui_CalendarioDialog()  # Crear la instancia de la interfaz de calendario
        self.ui_calendario.setupUi(self.calendario_dialog)  # Configurar la interfaz

        # Conectar el botón de "Ok" para asignar la fecha seleccionada al campo de fecha
        self.ui_calendario.button_ok.clicked.connect(
            lambda: self.asignarFechaHora(self.ui_calendario)
        )

        self.calendario_dialog.exec_()  # Mostrar el calendario

    # Metodo para asignar la fecha seleccionada al campo de texto
    def asignarFechaHora(self, calendario_ui):
        # Captura la fecha seleccionada y la hora actual
        fecha_seleccionada = calendario_ui.calendarWidget.selectedDate()
        hora_seleccionada = calendario_ui.time_edit.time()

        # Combina la fecha y hora en el formato deseado
        fecha_hora = f"{fecha_seleccionada.toString('dd/MM/yyyy')} {hora_seleccionada.toString('HH:mm')}"

        # Asigna la fecha y hora al QTextEdit
        self.fecha.setDateTime(QDateTime.fromString(fecha_hora, "dd/MM/yyyy HH:mm"))
        self.calendario_dialog.accept()  # Cierra el diálogo


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textoagregarrecordatorio.setText(QCoreApplication.translate("MainWindow", u"Agregar Recordatorio", None))
        self.texto_Recordatorio.setText(QCoreApplication.translate("MainWindow", u"Recordatorio", None))
#if QT_CONFIG(whatsthis)
        self.Botonguardar.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guardar</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Botonguardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.iconocalendario.setText("")
        self.iconocampana.setText("")
        self.recordatorioError.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarRecordatorio_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(AgregarRecordatorio_MainWindow)
    AgregarRecordatorio_MainWindow.show()
    sys.exit(app.exec_())
