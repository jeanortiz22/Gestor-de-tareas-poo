from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalendarioDialog(object):
    def setupUi(self, CalendarioDialog):
        CalendarioDialog.setObjectName("CalendarioDialog")
        CalendarioDialog.resize(400, 300)

        # Calendario
        self.calendarWidget = QtWidgets.QCalendarWidget(CalendarioDialog)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 40, 312, 183))
        self.calendarWidget.setStyleSheet(
            "selection-background-color: rgb(170, 255, 0);\n"
            "font: 75 9pt \"MS Shell Dlg 2\";"
        )
        self.calendarWidget.setObjectName("calendarWidget")

        # Editor de Hora
        self.time_edit = QtWidgets.QTimeEdit(CalendarioDialog)
        self.time_edit.setGeometry(QtCore.QRect(130, 230, 141, 21))
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setObjectName("time_edit")

        # Botón Aceptar
        self.button_ok = QtWidgets.QPushButton(CalendarioDialog)
        self.button_ok.setGeometry(QtCore.QRect(160, 260, 75, 23))
        self.button_ok.setObjectName("button_ok")
        self.button_ok.setText("Aceptar")

        # Establecer la fecha mínima como la fecha actual
        fecha_actual = QtCore.QDate.currentDate()
        self.calendarWidget.setMinimumDate(fecha_actual)

        self.retranslateUi(CalendarioDialog)
        QtCore.QMetaObject.connectSlotsByName(CalendarioDialog)

    def retranslateUi(self, CalendarioDialog):
        _translate = QtCore.QCoreApplication.translate
        CalendarioDialog.setWindowTitle(_translate("CalendarioDialog", "Calendario"))
