from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Backend.Tarea import Tarea  # Importar la clase Tarea desde el backend

class Ui_BuscarTareaMainWindow(object):
    def setupUi(self, BuscarTareaMainWindow):
        BuscarTareaMainWindow.setObjectName("BuscarTareaMainWindow")
        BuscarTareaMainWindow.resize(1800, 880)
        BuscarTareaMainWindow.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                            "background-color: rgb(211, 211, 211);")
        self.centralwidget = QtWidgets.QWidget(BuscarTareaMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Etiqueta de Bienvenida
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 70, 701, 41))
        self.label_3.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        # Campo de búsqueda
        self.BuscarTarea = QtWidgets.QLineEdit(self.centralwidget)
        self.BuscarTarea.setGeometry(QtCore.QRect(270, 220, 341, 41))
        self.BuscarTarea.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 15pt \"MS Shell Dlg 2\";")
        self.BuscarTarea.setObjectName("BuscarTarea")

        # Área de desplazamiento para mostrar las tareas
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(270, 290, 881, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 879, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Layout para las tareas
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Nombre del usuario
        self.Nombredepersona = QtWidgets.QLabel(self.centralwidget)
        self.Nombredepersona.setGeometry(QtCore.QRect(260, 120, 211, 41))
        self.Nombredepersona.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.Nombredepersona.setObjectName("Nombredepersona")

        BuscarTareaMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BuscarTareaMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 21))
        self.menubar.setObjectName("menubar")
        BuscarTareaMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BuscarTareaMainWindow)
        self.statusbar.setObjectName("statusbar")
        BuscarTareaMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BuscarTareaMainWindow)
        QtCore.QMetaObject.connectSlotsByName(BuscarTareaMainWindow)

        # Conectar la búsqueda al cuadro de texto
        self.BuscarTarea.textChanged.connect(lambda: self.buscarTarea(1))  # Cambia el ID del usuario según tu implementación

    def retranslateUi(self, BuscarTareaMainWindow):
        _translate = QtCore.QCoreApplication.translate
        BuscarTareaMainWindow.setWindowTitle(_translate("BuscarTareaMainWindow", "Buscar Tarea"))
        self.label_3.setText(_translate("BuscarTareaMainWindow", "Bienvenido a tu gestor de tareas"))
        self.Nombredepersona.setText(_translate("BuscarTareaMainWindow", "Usuario"))

    def buscarTarea(self, id_usuario):
        busqueda = self.BuscarTarea.text().strip()

        if busqueda == "":
            return  # No buscar si no hay texto

        tareas = Tarea()
        tareas_encontradas = tareas.buscar_tareas(id_usuario, busqueda)

        # Limpiar el área de desplazamiento
        for i in reversed(range(self.scrollLayout.count())):
            widget = self.scrollLayout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Mostrar las tareas encontradas
        for tarea in tareas_encontradas:
            tarea_widget = self.crearWidgetTarea(tarea)
            self.scrollLayout.addWidget(tarea_widget)

    def crearWidgetTarea(self, tarea):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Título
        titulo = QtWidgets.QLabel(tarea['titulo'])
        titulo.setStyleSheet("font: 16pt; font-weight: bold;")
        layout.addWidget(titulo)

        # Descripción
        descripcion = QtWidgets.QLabel(tarea['descripcion'])
        descripcion.setWordWrap(True)
        layout.addWidget(descripcion)

        # Fecha de vencimiento
        fecha_vencimiento = QtWidgets.QLabel(f"Fecha de vencimiento: {tarea['fecha_vencimiento']}")
        layout.addWidget(fecha_vencimiento)

        widget.setLayout(layout)
        return widget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuscarTareaMainWindow = QtWidgets.QMainWindow()
    ui = Ui_BuscarTareaMainWindow()
    ui.setupUi(BuscarTareaMainWindow)
    BuscarTareaMainWindow.show()
    sys.exit(app.exec_())
