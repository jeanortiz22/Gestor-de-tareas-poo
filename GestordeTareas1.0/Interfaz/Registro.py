# main.py
from os import close

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from usuario import Usuarios  # Asegúrate de que el archivo se llame usuarios.py y esté en el mismo directorio

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 689)
        MainWindow.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 130, 371, 461))
        self.widget.setStyleSheet("background-color: rgb(190, 190, 190);\n"
                                  "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.Nombre = QtWidgets.QLineEdit(self.widget)  # Cambiar a QLineEdit para texto de una sola línea
        self.Nombre.setGeometry(QtCore.QRect(60, 40, 241, 41))
        self.Nombre.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                  "font: 14pt \"MS Shell Dlg 2\";")
        self.Nombre.setObjectName("Nombre")
        self.Correo = QtWidgets.QLineEdit(self.widget)  # Cambiar a QLineEdit
        self.Correo.setGeometry(QtCore.QRect(60, 120, 241, 41))
        self.Correo.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                  "font: 14pt \"MS Shell Dlg 2\";")
        self.Correo.setObjectName("Correo")
        self.Contrasena = QtWidgets.QLineEdit(self.widget)  # Cambiar a QLineEdit
        self.Contrasena.setGeometry(QtCore.QRect(60, 210, 241, 41))
        self.Contrasena.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                      "font: 14pt \"MS Shell Dlg 2\";")
        self.Contrasena.setEchoMode(QtWidgets.QLineEdit.Password)  # Ocultar contraseña
        self.Contrasena.setObjectName("Contrasena")
        self.Contrasena_2 = QtWidgets.QLineEdit(self.widget)  # Cambiar a QLineEdit
        self.Contrasena_2.setGeometry(QtCore.QRect(60, 310, 241, 41))
        self.Contrasena_2.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                        "font: 14pt \"MS Shell Dlg 2\";")
        self.Contrasena_2.setEchoMode(QtWidgets.QLineEdit.Password)  # Ocultar contraseña
        self.Contrasena_2.setObjectName("Contrasena_2")
        self.Registro = QtWidgets.QPushButton(self.widget)
        self.Registro.setGeometry(QtCore.QRect(100, 370, 151, 41))
        self.Registro.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                    "font: 87 12pt \"Segoe UI Black\";")
        self.Registro.setObjectName("Registro")
        self.Registrarse_2 = QtWidgets.QLabel(self.widget)
        self.Registrarse_2.setEnabled(True)
        self.Registrarse_2.setGeometry(QtCore.QRect(60, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Registrarse_2.setFont(font)
        self.Registrarse_2.setStyleSheet("color: rgb(231, 231, 231);\n"
                                         "font: 87 12pt \"Arial Black\";\n"
                                         "background-color: rgb(190, 190, 190);\n"
                                         "")
        self.Registrarse_2.setTextFormat(QtCore.Qt.PlainText)
        self.Registrarse_2.setObjectName("Registrarse_2")
        self.Registrarse_3 = QtWidgets.QLabel(self.widget)
        self.Registrarse_3.setEnabled(True)
        self.Registrarse_3.setGeometry(QtCore.QRect(60, 90, 91, 21))
        self.Registrarse_3.setFont(font)
        self.Registrarse_3.setStyleSheet("color: rgb(231, 231, 231);\n"
                                         "font: 87 12pt \"Arial Black\";\n"
                                         "background-color: rgb(190, 190, 190);\n"
                                         "")
        self.Registrarse_3.setTextFormat(QtCore.Qt.PlainText)
        self.Registrarse_3.setObjectName("Registrarse_3")
        self.Registrarse_4 = QtWidgets.QLabel(self.widget)
        self.Registrarse_4.setEnabled(True)
        self.Registrarse_4.setGeometry(QtCore.QRect(60, 180, 200, 21))
        self.Registrarse_4.setFont(font)
        self.Registrarse_4.setStyleSheet("color: rgb(231, 231, 231);\n"
                                         "font: 87 12pt \"Arial Black\";\n"
                                         "background-color: rgb(190, 190, 190);\n"
                                         "")
        self.Registrarse_4.setTextFormat(QtCore.Qt.PlainText)
        self.Registrarse_4.setObjectName("Registrarse_4")
        self.Registrarse_5 = QtWidgets.QLabel(self.widget)
        self.Registrarse_5.setEnabled(True)
        self.Registrarse_5.setGeometry(QtCore.QRect(60, 280, 201, 21))
        self.Registrarse_5.setFont(font)
        self.Registrarse_5.setStyleSheet("color: rgb(231, 231, 231);\n"
                                         "font: 87 12pt \"Arial Black\";\n"
                                         "background-color: rgb(190, 190, 190);\n"
                                         "")
        self.Registrarse_5.setTextFormat(QtCore.Qt.PlainText)
        self.Registrarse_5.setObjectName("Registrarse_5")
        self.Registrarse = QtWidgets.QLabel(self.centralwidget)
        self.Registrarse.setEnabled(True)
        self.Registrarse.setGeometry(QtCore.QRect(300, 70, 371, 68))
        self.Registrarse.setFont(QtGui.QFont("Arial Black", 36))
        self.Registrarse.setStyleSheet("color: rgb(231, 231, 231);\n"
                                       "font: 87 36pt \"Arial Black\";\n"
                                       "background-color: rgb(190, 190, 190);\n"
                                       "")
        self.Registrarse.setTextFormat(QtCore.Qt.PlainText)
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

        # Conectar el botón a la función de registro

        self.Registro.clicked.connect(self.registrarusuarios)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registro de Usuarios"))
        self.Registro.setText(_translate("MainWindow", "Registrarse"))
        self.Registrarse_2.setText(_translate("MainWindow", "Nombre"))
        self.Registrarse_3.setText(_translate("MainWindow", "Email"))
        self.Registrarse_4.setText(_translate("MainWindow", "Contraseña"))  # Corregido aquí
        self.Registrarse_5.setText(_translate("MainWindow", "Confirmar Contraseña"))  # Corregido aquí
        self.Registrarse.setText(_translate("MainWindow", "Registrarse"))

    def registrarusuarios(self):
        nombre = self.Nombre.text()
        correo = self.Correo.text()
        contrasena = self.Contrasena.text()
        confirmar_contrasena = self.Contrasena_2.text()


        if contrasena != confirmar_contrasena:
            QMessageBox.warning(None, "Error", "Las contraseñas no coinciden.")
            return

        # Crear instancia de Usuarios y asignar datos
        usuario = Usuarios(nombre, correo, contrasena)

        # Registrar el usuario
        registro_exitoso = usuario.registrarusuarios()

        if registro_exitoso:
            print("Usuario registrado correctamente desde la interfaz gráfica.")
            self.centralwidget.window().hide() #oculta la ventana de registro en vez de cerrarla

        else:
            print("Error al registrar el usuario desde la interfaz gráfica.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
