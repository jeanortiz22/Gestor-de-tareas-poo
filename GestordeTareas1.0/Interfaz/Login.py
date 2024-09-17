from PyQt5 import QtCore, QtGui, QtWidgets
from Registro import Ui_MainWindow as UiRegistroWindow
from usuario import Usuarios


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 689)
        MainWindow.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(340, 240, 371, 271))
        self.widget.setStyleSheet("background-color: rgb(190, 190, 190);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.Correo = QtWidgets.QLineEdit(self.widget)
        self.Correo.setGeometry(QtCore.QRect(50, 40, 241, 41))
        self.Correo.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Correo.setObjectName("Correo")
        self.Contrasena = QtWidgets.QLineEdit(self.widget)
        self.Contrasena.setGeometry(QtCore.QRect(50, 120, 241, 41))
        self.Contrasena.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Contrasena.setObjectName("Contrasena")
        self.Registro = QtWidgets.QPushButton(self.widget)
        self.Registro.setGeometry(QtCore.QRect(90, 180, 151, 41))
        self.Registro.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.Registro.setObjectName("Registro")
        self.Registrarse_3 = QtWidgets.QLabel(self.widget)
        self.Registrarse_3.setEnabled(True)
        self.Registrarse_3.setGeometry(QtCore.QRect(50, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Registrarse_3.setFont(font)
        self.Registrarse_3.setStyleSheet("color: rgb(231, 231, 231);\n"
"\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(190, 190, 190);\n"
"\n"
"")
        self.Registrarse_3.setTextFormat(QtCore.Qt.PlainText)
        self.Registrarse_3.setObjectName("Registrarse_3")
        self.Registrarse_4 = QtWidgets.QLabel(self.widget)
        self.Registrarse_4.setEnabled(True)
        self.Registrarse_4.setGeometry(QtCore.QRect(50, 90, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Registrarse_4.setFont(font)
        self.Registrarse_4.setStyleSheet("color: rgb(231, 231, 231);\n"
"\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(190, 190, 190);\n"
"\n"
"")
        self.Registrarse_4.setTextFormat(QtCore.Qt.PlainText)
        self.Registrarse_4.setObjectName("Registrarse_4")
        self.Registrarse = QtWidgets.QLabel(self.centralwidget)
        self.Registrarse.setEnabled(True)
        self.Registrarse.setGeometry(QtCore.QRect(340, 180, 371, 68))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Registrarse.setFont(font)
        self.Registrarse.setStyleSheet("color: rgb(231, 231, 231);\n"
"\n"
"font: 87 28pt \"Arial Black\";\n"
"background-color: rgb(190, 190, 190);\n"
"\n"
"")
        self.Registrarse.setTextFormat(QtCore.Qt.PlainText)
        self.Registrarse.setIndent(0)
        self.Registrarse.setObjectName("Registrarse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Registro.clicked.connect(self.inicioSeccion)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Registro.setText(_translate("MainWindow", "Ingresar"))
        self.Registrarse_3.setText(_translate("MainWindow", "Email"))
        self.Registrarse_4.setText(_translate("MainWindow", "Contrasena"))
        self.Registrarse.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/>hhh</p></body></html>"))
        self.Registrarse.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Registrarse.setText(_translate("MainWindow", "Inicio de Seccion"))


    def inicioSeccion(self):
        correo = self.Correo.text()
        contrasena = self.Contrasena.text()

        usuario = Usuarios()

        registrar = usuario.login(correo,contrasena)


        if registrar:
            print("Inicio de seccion exitoso")

        else :
            self.AbrirRegistro()



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
