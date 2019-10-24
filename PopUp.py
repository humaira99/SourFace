# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(449, 303)
        Dialog.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"font: 12pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 427, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 75 14pt \"Century Gothic\";\n"
"color: rgb(200, 200, 200);\n"
"font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 75 14pt \"Century Gothic\";\n"
"color: rgb(200, 200, 200);\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.listWidget_taste = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_taste.setStyleSheet("")
        self.listWidget_taste.setObjectName("listWidget_taste")
        self.gridLayout.addWidget(self.listWidget_taste, 1, 0, 1, 1)
        self.listWidget_emotion = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_emotion.setStyleSheet("font-weight: regular;")
        self.listWidget_emotion.setObjectName("listWidget_emotion")
        self.gridLayout.addWidget(self.listWidget_emotion, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Emotion Predominantly: "))
        self.label_2.setText(_translate("Dialog", "Taste Predominantly: "))
