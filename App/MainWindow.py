# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.enableReminder = QtWidgets.QCheckBox(self.centralwidget)
        self.enableReminder.setMinimumSize(QtCore.QSize(200, 100))
        self.enableReminder.setObjectName("enableReminder")
        self.gridLayout_3.addWidget(self.enableReminder, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 20, 93, 184))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s5 = QtWidgets.QRadioButton(self.widget)
        self.s5.setObjectName("s5")
        self.verticalLayout.addWidget(self.s5)
        self.s10 = QtWidgets.QRadioButton(self.widget)
        self.s10.setObjectName("s10")
        self.verticalLayout.addWidget(self.s10)
        self.m10 = QtWidgets.QRadioButton(self.widget)
        self.m10.setObjectName("m10")
        self.verticalLayout.addWidget(self.m10)
        self.m20 = QtWidgets.QRadioButton(self.widget)
        self.m20.setObjectName("m20")
        self.verticalLayout.addWidget(self.m20)
        self.m30 = QtWidgets.QRadioButton(self.widget)
        self.m30.setObjectName("m30")
        self.verticalLayout.addWidget(self.m30)
        self.m40 = QtWidgets.QRadioButton(self.widget)
        self.m40.setObjectName("m40")
        self.verticalLayout.addWidget(self.m40)
        self.h1 = QtWidgets.QRadioButton(self.widget)
        self.h1.setObjectName("h1")
        self.verticalLayout.addWidget(self.h1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.disableReminder = QtWidgets.QCheckBox(self.groupBox)
        self.disableReminder.setObjectName("disableReminder")
        self.gridLayout_2.addWidget(self.disableReminder, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_2.addWidget(self.timeEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.verticalLayout_3.addWidget(self.timeEdit_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkSunday = QtWidgets.QCheckBox(self.groupBox)
        self.checkSunday.setObjectName("checkSunday")
        self.gridLayout.addWidget(self.checkSunday, 0, 0, 1, 1)
        self.checkThursday = QtWidgets.QCheckBox(self.groupBox)
        self.checkThursday.setObjectName("checkThursday")
        self.gridLayout.addWidget(self.checkThursday, 0, 1, 1, 1)
        self.checkMonday = QtWidgets.QCheckBox(self.groupBox)
        self.checkMonday.setObjectName("checkMonday")
        self.gridLayout.addWidget(self.checkMonday, 1, 0, 1, 1)
        self.checkFriday = QtWidgets.QCheckBox(self.groupBox)
        self.checkFriday.setObjectName("checkFriday")
        self.gridLayout.addWidget(self.checkFriday, 1, 1, 1, 1)
        self.checkTuesday = QtWidgets.QCheckBox(self.groupBox)
        self.checkTuesday.setObjectName("checkTuesday")
        self.gridLayout.addWidget(self.checkTuesday, 2, 0, 1, 1)
        self.checkSaturday = QtWidgets.QCheckBox(self.groupBox)
        self.checkSaturday.setObjectName("checkSaturday")
        self.gridLayout.addWidget(self.checkSaturday, 2, 1, 1, 1)
        self.checkWednesday = QtWidgets.QCheckBox(self.groupBox)
        self.checkWednesday.setObjectName("checkWednesday")
        self.gridLayout.addWidget(self.checkWednesday, 3, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)
        self.reminder_label = QtWidgets.QLabel(self.centralwidget)
        self.reminder_label.setMinimumSize(QtCore.QSize(200, 100))
        self.reminder_label.setObjectName("reminder_label")
        self.gridLayout_3.addWidget(self.reminder_label, 3, 0, 1, 1)
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setObjectName("helpButton")
        self.gridLayout_3.addWidget(self.helpButton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enableReminder.setText(_translate("MainWindow", "Enable Reminder"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Time interval"))
        self.s5.setText(_translate("MainWindow", "5 seconds"))
        self.s10.setText(_translate("MainWindow", "10 seconds"))
        self.m10.setText(_translate("MainWindow", "10 minutes"))
        self.m20.setText(_translate("MainWindow", "20 minutes"))
        self.m30.setText(_translate("MainWindow", "30 minutes"))
        self.m40.setText(_translate("MainWindow", "40 minutes"))
        self.h1.setText(_translate("MainWindow", "1 hour"))
        self.groupBox.setTitle(_translate("MainWindow", "Disable"))
        self.disableReminder.setText(_translate("MainWindow", "disable in these timings"))
        self.label.setText(_translate("MainWindow", "From"))
        self.label_2.setText(_translate("MainWindow", "To"))
        self.label_3.setText(_translate("MainWindow", "On days"))
        self.checkSunday.setText(_translate("MainWindow", "Sunday"))
        self.checkThursday.setText(_translate("MainWindow", "Thursday"))
        self.checkMonday.setText(_translate("MainWindow", "Monday"))
        self.checkFriday.setText(_translate("MainWindow", "Friday"))
        self.checkTuesday.setText(_translate("MainWindow", "Tuesday"))
        self.checkSaturday.setText(_translate("MainWindow", "Saturday"))
        self.checkWednesday.setText(_translate("MainWindow", "Wednesday"))
        self.reminder_label.setText(_translate("MainWindow", "Reminder"))
        self.helpButton.setText(_translate("MainWindow", "Help"))

