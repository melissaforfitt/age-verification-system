# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self-service-checkout-design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_self_service_checkout_window(object):
    def setupUi(self, self_service_checkout_window):
        self_service_checkout_window.setObjectName("self_service_checkout_window")
        self_service_checkout_window.resize(512, 450)
        self.centralwidget = QtWidgets.QWidget(self_service_checkout_window)
        self.centralwidget.setObjectName("centralwidget")
        self.camera_window = QtWidgets.QGraphicsView(self.centralwidget)
        self.camera_window.setGeometry(QtCore.QRect(130, 60, 256, 192))
        self.camera_window.setObjectName("camera_window")
        self.camera_instruction_label = QtWidgets.QLabel(self.centralwidget)
        self.camera_instruction_label.setGeometry(QtCore.QRect(140, 260, 241, 16))
        self.camera_instruction_label.setObjectName("camera_instruction_label")
        self.select_item_label = QtWidgets.QLabel(self.centralwidget)
        self.select_item_label.setGeometry(QtCore.QRect(70, 290, 101, 16))
        self.select_item_label.setObjectName("select_item_label")
        self.cider_button = QtWidgets.QPushButton(self.centralwidget)
        self.cider_button.setGeometry(QtCore.QRect(190, 290, 56, 17))
        self.cider_button.setObjectName("cider_button")
        self.bread_button = QtWidgets.QPushButton(self.centralwidget)
        self.bread_button.setGeometry(QtCore.QRect(270, 290, 56, 17))
        self.bread_button.setObjectName("bread_button")
        self.milk_button = QtWidgets.QPushButton(self.centralwidget)
        self.milk_button.setGeometry(QtCore.QRect(350, 290, 56, 17))
        self.milk_button.setObjectName("milk_button")
        self.decision_window = QtWidgets.QTextEdit(self.centralwidget)
        self.decision_window.setGeometry(QtCore.QRect(220, 340, 104, 64))
        self.decision_window.setObjectName("decision_window")
        self.decision_label = QtWidgets.QLabel(self.centralwidget)
        self.decision_label.setGeometry(QtCore.QRect(170, 370, 41, 16))
        self.decision_label.setObjectName("decision_label")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(150, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self_service_checkout_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self_service_checkout_window)
        self.statusbar.setObjectName("statusbar")
        self_service_checkout_window.setStatusBar(self.statusbar)

        self.retranslateUi(self_service_checkout_window)
        QtCore.QMetaObject.connectSlotsByName(self_service_checkout_window)

    def retranslateUi(self, self_service_checkout_window):
        _translate = QtCore.QCoreApplication.translate
        self_service_checkout_window.setWindowTitle(_translate("self_service_checkout_window", "Self-Service Checkout"))
        self.camera_instruction_label.setText(_translate("self_service_checkout_window", "Please make sure that you are positioned within the frame above."))
        self.select_item_label.setText(_translate("self_service_checkout_window", "Select an item to purchase:"))
        self.cider_button.setText(_translate("self_service_checkout_window", "Cider"))
        self.bread_button.setText(_translate("self_service_checkout_window", "Bread"))
        self.milk_button.setText(_translate("self_service_checkout_window", "Milk"))
        self.decision_label.setText(_translate("self_service_checkout_window", "Decision:"))
        self.title_label.setText(_translate("self_service_checkout_window", "Self-Service Checkout"))

