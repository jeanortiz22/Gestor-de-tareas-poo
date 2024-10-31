from PyQt5 import QtCore, QtGui, QtWidgets
from RegistroNuevo import Ui_MainWindow as UiRegistroWindow
from Interfaz.Paginaprincipal import Ui_MainWindow as UiPrincipalWindow

from Backend.usuario import Usuarios


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 800))
        MainWindow.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(380, 250, 371, 291))
        self.widget.setStyleSheet("background-color: rgb(190, 190, 190);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.INCorreo = QtWidgets.QTextEdit(self.widget)
        self.INCorreo.setEnabled(True)
        self.INCorreo.setGeometry(QtCore.QRect(50, 40, 241, 41))
        self.INCorreo.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.INCorreo.setObjectName("INCorreo")
        self.INContrasena = QtWidgets.QLineEdit(self.widget)
        self.INContrasena.setGeometry(QtCore.QRect(50, 120, 241, 41))
        self.INContrasena.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.INContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.INContrasena.setObjectName("INContrasena")


        self.Ingresarboton = QtWidgets.QPushButton(self.widget)
        self.Ingresarboton.setGeometry(QtCore.QRect(100, 190, 151, 41))
        self.Ingresarboton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.Ingresarboton.setObjectName("Ingresarboton")
        # Nuevo botón "¿No estás registrado? Registrarse"
        self.Registroboton = QtWidgets.QPushButton(self.widget)
        self.Registroboton.setGeometry(QtCore.QRect(50, 240, 271, 50))
        self.Registroboton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                         "background-color: rgb(190, 190, 190);")
        self.Registroboton.setFlat(True)  # Para que parezca texto y no un botón tradicional
        self.Registroboton.setObjectName("Registroboton")

        self.Email = QtWidgets.QLabel(self.widget)
        self.Email.setEnabled(True)
        self.Email.setGeometry(QtCore.QRect(50, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Email.setFont(font)
        self.Email.setStyleSheet("color: rgb(231, 231, 231);\n"
"\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(190, 190, 190);\n"
"\n"
"")

        self.Email.setObjectName("Email")
        self.Contrasena = QtWidgets.QLabel(self.widget)
        self.Contrasena.setEnabled(True)
        self.Contrasena.setGeometry(QtCore.QRect(50, 90, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Contrasena.setFont(font)
        self.Contrasena.setStyleSheet("color: rgb(231, 231, 231);\n"
"\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(190, 190, 190);\n"
"\n"
"")
        self.Contrasena.setTextFormat(QtCore.Qt.PlainText)
        self.Contrasena.setObjectName("Contrasena")

        self.MensajeEmergente = QtWidgets.QLabel(self.widget)
        self.MensajeEmergente.setGeometry(QtCore.QRect(50, 165, 251, 21))
        self.MensajeEmergente.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 4);")
        self.MensajeEmergente.setAlignment(QtCore.Qt.AlignCenter)
        self.MensajeEmergente.setObjectName("MensajeEmergente")

        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setEnabled(True)
        self.Titulo.setGeometry(QtCore.QRect(380, 190, 371, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("color: rgb(231, 231, 231);\n"
"\n"
"font: 87 28pt \"Arial Black\";\n"
"background-color: rgb(190, 190, 190);\n"
"\n"
"")
        self.Titulo.setTextFormat(QtCore.Qt.PlainText)
        self.Titulo.setIndent(0)
        self.Titulo.setObjectName("Titulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Ingresarboton.clicked.connect(self.inicioSeccion)
        self.Registroboton.clicked.connect(self.AbrirRegistro)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Ingresarboton.setText(_translate("MainWindow", "Ingresesar"))
        self.Registroboton.setText(_translate("MainWindow", "¿No estás registrado? Registrarse"))
        self.Email.setText(_translate("MainWindow", "Email"))
        self.Contrasena.setText(_translate("MainWindow", "Contrasena"))
        self.MensajeEmergente.setText(_translate("MainWindow", "MensajeEmergente"))
        self.MensajeEmergente.setText("")
        self.Titulo.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/>hhh</p></body></html>"))
        self.Titulo.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Titulo.setText(_translate("MainWindow", "Inicio de sesión"))

    def inicioSeccion(self):
        correo = self.INCorreo.toPlainText().strip()
        contrasena = self.INContrasena.text()
        usuario = Usuarios()
        exito,mensaje, nombre = usuario.login(correo, contrasena)

        if exito:
            id_usuario = mensaje
            QtWidgets.QApplication.instance().activeWindow().close() ## cierra la ventana activa hasta el momento
            self.AbrirPrincipal(id_usuario,nombre)
        else:
            self.MensajeEmergente.setText(mensaje)


    def AbrirPrincipal(self,id_usuario, nombre):
        self.window = QtWidgets.QMainWindow()  # Crear una nueva ventana
        self.ui = UiPrincipalWindow()  # Usar la clase del formulario "Untitled"
        self.ui.setupUi(self.window, id_usuario, nombre)  # Inicializar la ventana de "Untitled"
        self.window.show()  # Mostrar la ventana


    def AbrirRegistro(self):
        self.window = QtWidgets.QMainWindow()  # Crear una nueva ventana
        self.ui = UiRegistroWindow()  # Usar la clase de la segunda ventana
        self.ui.setupUi(self.window)  # Inicializar la segunda ventana
        self.window.show()  # Mostrar la ventana




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
