from Interfaz.LoginNuevo import Ui_MainWindow

from PyQt5 import QtWidgets

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Crear la ventana principal
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Mostrar la ventana principal
    MainWindow.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
