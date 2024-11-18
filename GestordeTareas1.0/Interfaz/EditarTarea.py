from PyQt5 import QtCore, QtGui, QtWidgets
from Backend.Tarea import Tarea
from Calendario1 import Ui_CalendarioDialog
import re


class Ui_Editar_MainWindow(object):
    def setupUi(self, Agregar_MainWindow,id_tarea,id_usuario,mostrar_tareas):

        self.mostrar_tareas = mostrar_tareas

        Agregar_MainWindow.setObjectName("Agregar_MainWindow")
        Agregar_MainWindow.resize(1001, 625)
        Agregar_MainWindow.setMouseTracking(False)
        Agregar_MainWindow.setMaximumSize(QtCore.QSize(1001, 625))
        self.centralwidget = QtWidgets.QWidget(Agregar_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Texto_Agregar = QtWidgets.QLabel(self.centralwidget)
        self.Texto_Agregar.setGeometry(QtCore.QRect(90, 60,10000, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Texto_Agregar.setFont(font)
        self.Texto_Agregar.setObjectName("Texto_Agregar")

        self.Ingresar_Nombre_Tarea = QtWidgets.QTextEdit(self.centralwidget)
        self.Ingresar_Nombre_Tarea.setGeometry(QtCore.QRect(100, 150, 791, 51))
        self.Ingresar_Nombre_Tarea.setObjectName("Ingresar_Nombre_Tarea")

        self.Ingresar_Descripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.Ingresar_Descripcion.setGeometry(QtCore.QRect(100, 260, 791, 101))
        self.Ingresar_Descripcion.setObjectName("Ingresar_Descripcion")
        self.Ingresar_Descripcion.setStyleSheet(u"QLineEdit{\n"
                                    "	border-radius:15px;\n"
                                    "}")

        self.Guardar_Tarea = QtWidgets.QPushButton(self.centralwidget)
        self.Guardar_Tarea.setEnabled(True)
        self.Guardar_Tarea.setGeometry(QtCore.QRect(100, 500, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Guardar_Tarea.setFont(font)
        self.Guardar_Tarea.setAcceptDrops(False)
        self.Guardar_Tarea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Guardar_Tarea.setObjectName("Guardar_Tarea")
        self.Guardar_Tarea.setStyleSheet(u"QPushButton {\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	border-radius:15px;\n"
                                        "	background-color: rgb(30, 30, 30);\n"
                                        "}\n"
                                        "QPushButton:Hover {\n"
                                        "	border-bottom: 2px solid blue;\n"
                                        "	background-color: rgb(30, 30, 30);\n"
                                        "\n"
                                        "}")
        self.Guardar_Tarea.clicked.connect(lambda: self.EditarTarea(id_tarea, id_usuario,self.obtenerFechaHora()))



        self.Texto_Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Texto_Titulo.setGeometry(QtCore.QRect(100, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Texto_Titulo.setFont(font)
        self.Texto_Titulo.setObjectName("Texto_Titulo")
        self.Texto_Descripcion = QtWidgets.QLabel(self.centralwidget)
        self.Texto_Descripcion.setGeometry(QtCore.QRect(100, 230, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Texto_Descripcion.setFont(font)
        self.Texto_Descripcion.setObjectName("Texto_Descripcion")
        self.Texto_Fecha = QtWidgets.QLabel(self.centralwidget)
        self.Texto_Fecha.setGeometry(QtCore.QRect(100, 390, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Texto_Fecha.setFont(font)
        self.Texto_Fecha.setObjectName("Texto_Fecha")
        self.Seleccionar_Fecha = QtWidgets.QTextEdit(self.centralwidget)
        self.Seleccionar_Fecha.setEnabled(True)
        self.Seleccionar_Fecha.setGeometry(QtCore.QRect(100, 420, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Seleccionar_Fecha.setFont(font)
        self.Seleccionar_Fecha.setAcceptDrops(False)
        self.Seleccionar_Fecha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Seleccionar_Fecha.setText("")
        self.Seleccionar_Fecha.setObjectName("Seleccionar_Fecha")
        self.Seleccionar_Fecha.setStyleSheet(u"QLineEdit{\n"
                                    "	border-radius:15px;\n"
                                    "}")
        self.Mensaje_Resultado = QtWidgets.QLabel(self.centralwidget)
        self.Mensaje_Resultado.setGeometry(QtCore.QRect(100, 560, 791, 30))  # Ajusta la posición según sea necesario
        self.Mensaje_Resultado.setFont(font)
        self.Mensaje_Resultado.setObjectName("Mensaje_Resultado")
        self.Mensaje_Resultado.setStyleSheet("color: red;")  # Puedes cambiar el color según prefieras

        Agregar_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Agregar_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 21))
        self.menubar.setObjectName("menubar")
        Agregar_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Agregar_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Agregar_MainWindow.setStatusBar(self.statusbar)

        # Agregando botón de calendario
        self.Boton_Calendario = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Calendario.setGeometry(QtCore.QRect(842, 420, 51, 51))  # Ajusta la posición
        self.Boton_Calendario.setText("📅")
        self.Boton_Calendario.setFont(font)
        self.Boton_Calendario.setObjectName("Boton_Calendario")
        self.Boton_Calendario.clicked.connect(self.abrirCalendario)
        self.Boton_Calendario.setStyleSheet(u"QLineEdit{\n"
                                    "	border-radius:15px;\n"
                                    "}")

        self.retranslateUi(Agregar_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Agregar_MainWindow)

    def retranslateUi(self, Agregar_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Agregar_MainWindow.setWindowTitle(_translate("Agregar_MainWindow", "Agregar Tarea"))
        self.Texto_Agregar.setText(_translate("Agregar_MainWindow", "Editar la Tarea"))
        self.Guardar_Tarea.setText(_translate("Agregar_MainWindow", "Guardar"))
        self.Texto_Titulo.setText(_translate("Agregar_MainWindow", "Nuevo titulo"))
        self.Texto_Descripcion.setText(_translate("Agregar_MainWindow", "Nueva descripción "))
        self.Texto_Fecha.setText(_translate("Agregar_MainWindow", "Nueva fecha limite"))

    def abrirCalendario(self):
        self.calendario_dialog = QtWidgets.QDialog()
        self.ui_calendario = Ui_CalendarioDialog()
        self.ui_calendario.setupUi(self.calendario_dialog)

        # Conectar el metodo para asignar la fecha y hora seleccionadas
        self.ui_calendario.button_ok.clicked.connect(
            lambda: self.asignarFechaHora(self.ui_calendario)
        )

        self.calendario_dialog.exec_()  # Muestra el diálogo del calendario

    def asignarFechaHora(self, calendario_ui):
        fecha_hora = f"{calendario_ui.calendarWidget.selectedDate().toString('dd/MM/yyyy')} {calendario_ui.time_edit.time().toString('HH:mm')}"
        self.Seleccionar_Fecha.setText(fecha_hora)  # Asignar la fecha y hora al QTextEdit
        self.calendario_dialog.accept()  # Cerrar el diálogo
        print(fecha_hora)

    def obtenerFechaHora(self):
        # Esta función devolverá la fecha y hora seleccionadas desde el QTextEdit
        return self.Seleccionar_Fecha.toPlainText().strip()


    def EditarTarea(self,id_tarea,id_usuario,fecha_hora):
        Ntitulo=self.Ingresar_Nombre_Tarea.toPlainText().strip()
        Ndescripcion=self.Ingresar_Descripcion.toPlainText().strip()

        formato_fecha = r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$"
        if not fecha_hora or not re.match(formato_fecha, fecha_hora):
            self.Mensaje_Resultado.setText("Fecha límite inválida. Use el formato 'dd/MM/yyyy HH:mm'.")
            return

        EdiUsuario = Tarea()
        print(fecha_hora)
        if fecha_hora == "":
            fecha_hora = None
        exito,mensaje = EdiUsuario.editar_tarea(id_tarea,id_usuario,Ntitulo,Ndescripcion,fecha_hora)

        if exito:
            self.mostrar_tareas(id_usuario)
            self.centralwidget.window().hide()


        else:
            self.Mensaje_Resultado.setText(mensaje)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Agregar_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Editar_MainWindow()
    ui.setupUi(Agregar_MainWindow)
    Agregar_MainWindow.show()
    sys.exit(app.exec_())
