from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalendarioDialog(object):
    def setupUi(self, CalendarioDialog):
        CalendarioDialog.setObjectName("CalendarioDialog")
        CalendarioDialog.resize(400, 300)
        self.calendarWidget = QtWidgets.QCalendarWidget(CalendarioDialog)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 40, 312, 183))
        self.calendarWidget.setStyleSheet("selection-background-color: rgb(170, 255, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateEdit = QtWidgets.QDateEdit(CalendarioDialog)
        self.dateEdit.setGeometry(QtCore.QRect(130, 250, 141, 21))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(CalendarioDialog)
        QtCore.QMetaObject.connectSlotsByName(CalendarioDialog)

    def retranslateUi(self, CalendarioDialog):
        _translate = QtCore.QCoreApplication.translate
        CalendarioDialog.setWindowTitle(_translate("CalendarioDialog", "Calendario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalendarioDialog = QtWidgets.QDialog()
    ui = Ui_CalendarioDialog()
    ui.setupUi(CalendarioDialog)
    CalendarioDialog.show()
    sys.exit(app.exec_())
