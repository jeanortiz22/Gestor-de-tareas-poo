from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QMetaObject,QRect, QSize,QDateTime)
from PyQt5.QtGui import ( QFont, QPixmap, QColor)
from PyQt5.QtWidgets import *
from Calendario1 import Ui_CalendarioDialog
from Backend.Recordatorio import Recordatorio, Escritorio
from datetime import datetime


import icono_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, id_tarea, id_usuario, fecha_vencimiento1,mostrar_tareas):
        self.mostrar_tareas =mostrar_tareas

        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 625)
        MainWindow.setMouseTracking(False)
        MainWindow.setMaximumSize(QSize(1001, 625))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textoagregarrecordatorio = QLabel(self.centralwidget)
        self.textoagregarrecordatorio.setObjectName(u"textoagregarrecordatorio")
        self.textoagregarrecordatorio.setGeometry(QRect(160, 40, 10000, 80))
        font1 = QFont()
        font1.setPointSize(20)
        self.textoagregarrecordatorio.setFont(font1)
        self.texto_Recordatorio = QLabel(self.centralwidget)
        self.texto_Recordatorio.setObjectName(u"texto_Recordatorio")
        self.texto_Recordatorio.setGeometry(QRect(170, 180, 301, 71))
        self.texto_Recordatorio.setFont(font1)
        self.Botonguardar = QPushButton(self.centralwidget)
        self.Botonguardar.setObjectName(u"Botonguardar")
        self.Botonguardar.setGeometry(QRect(110, 420, 791, 61))
        font2 = QFont()
        font2.setPointSize(16)
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
        self.Botonguardar.clicked.connect( lambda: self.guardar_recordatorio(id_tarea, id_usuario, fecha_vencimiento1, self.obtenerFechaHora()))

        # Crear botón de calendario
        self.botonCalendario = QPushButton(self.centralwidget)
        self.botonCalendario.setObjectName(u"botonCalendario")
        self.botonCalendario.setText("📅")
        self.botonCalendario.setGeometry(QRect(900, 290, 51, 51))  # Posicionamiento del botón
        self.botonCalendario.clicked.connect(self.abrirCalendario)  # Conectar el botón al metodo abrirCalendario

        self.iconocalendario = QLabel(self.centralwidget)
        self.iconocalendario.setObjectName(u"iconocalendario")
        self.iconocalendario.setGeometry(QRect(80, 50, 61, 61))
        self.iconocalendario.setPixmap(QPixmap(u":/icono/calendario.png"))
        self.iconocalendario.setScaledContents(True)
        self.iconocampana = QLabel(self.centralwidget)
        self.iconocampana.setObjectName(u"iconocampana")
        self.iconocampana.setGeometry(QRect(110, 180, 51, 51))
        self.iconocampana.setPixmap(QPixmap(u":/icono/campana.png"))
        self.iconocampana.setScaledContents(True)
        self.fecha = QTextEdit(self.centralwidget)
        self.fecha.setObjectName(u"fecha")
        self.fecha.setGeometry(QRect(110, 290, 791, 51))
        font3 = QFont()
        font3.setPointSize(14)
        self.fecha.setFont(font3)
        self.fecha.setStyleSheet(u"QTextEdit{\n"
                                 "    border-radius: 20px;\n"
                                 "    border: 6px solid #FFFFFF;\n"
                                 "    \n"
                                 "}")
        self.recordatorioError = QtWidgets.QLabel(self.centralwidget)
        self.recordatorioError.setObjectName(u"label")
        self.recordatorioError.setGeometry(QRect(117, 358, 771, 41))
        self.recordatorioError.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(255, 0, 4);")
        self.recordatorioError.setWordWrap(True)  # Permitir salto de línea automático
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
        # Obtener la fecha y la hora seleccionadas
        fecha_seleccionada = calendario_ui.calendarWidget.selectedDate()
        hora_seleccionada = calendario_ui.time_edit.time()

        # Crear el objeto QDateTime a partir de la fecha y hora seleccionadas
        fecha_hora = QDateTime(fecha_seleccionada, hora_seleccionada)

        # Convertir la fecha y hora al formato 'YYYY-MM-DD HH:MM:SS'
        fecha_hora_formateada = fecha_hora.toString("yyyy-MM-dd HH:mm:ss")

        # Asignar la fecha y hora formateada al QTextEdit
        self.fecha.setText(fecha_hora_formateada)
        self.calendario_dialog.accept()  # Cerrar el diálogo

    def obtenerFechaHora(self):
        # Esta función devolverá la fecha y hora seleccionadas desde el QTextEdit
        return self.fecha.toPlainText().strip()

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
        self.fecha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"YYYY-MM-DD  HH:MM:SS", None))
        self.recordatorioError.setText("")
    # retranslateUi

    def guardar_recordatorio(self, id_tarea, id_usuario, fecha_vencimiento1, fecha):
        try:
            # Convertimos las fechas de string a datetime
            fechamodi = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            self.recordatorioError.setText("Error: Formato de fecha inválido. Use 'YYYY-MM-DD HH:MM:SS'.")
            return

        print(fecha)
        print(fecha_vencimiento1)
        recordatorio1 = Recordatorio()
        verificar = Escritorio()

        exito, mensaje = recordatorio1.agregar_recordatorio(id_tarea, fechamodi, fecha_vencimiento1)

        if exito:
            print("Se agregó el recordatorio exitosamente")
            verificar.iniciar_verificacion_automatica()
            self.centralwidget.window().close()
            self.mostrar_tareas(id_usuario)
        else:
            self.recordatorioError.setText(mensaje)
            print("Error al agregar el recordatorio")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarRecordatorio_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(AgregarRecordatorio_MainWindow)
    AgregarRecordatorio_MainWindow.show()
    sys.exit(app.exec_())
