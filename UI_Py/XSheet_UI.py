# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XSheet_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XSheetUI(object):
    def setupUi(self, XSheetUI):
        XSheetUI.setObjectName("XSheetUI")
        XSheetUI.resize(243, 142)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(XSheetUI.sizePolicy().hasHeightForWidth())
        XSheetUI.setSizePolicy(sizePolicy)
        self.leftButton = QtWidgets.QPushButton(XSheetUI)
        self.leftButton.setGeometry(QtCore.QRect(10, 50, 51, 31))
        self.leftButton.setObjectName("leftButton")
        self.rightButton = QtWidgets.QPushButton(XSheetUI)
        self.rightButton.setGeometry(QtCore.QRect(180, 50, 51, 31))
        self.rightButton.setObjectName("rightButton")
        self.leftLabel = QtWidgets.QLabel(XSheetUI)
        self.leftLabel.setGeometry(QtCore.QRect(60, 50, 20, 31))
        self.leftLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.leftLabel.setObjectName("leftLabel")
        self.rightLabel = QtWidgets.QLabel(XSheetUI)
        self.rightLabel.setGeometry(QtCore.QRect(160, 50, 20, 31))
        self.rightLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.rightLabel.setObjectName("rightLabel")
        self.leftAddButton = QtWidgets.QPushButton(XSheetUI)
        self.leftAddButton.setGeometry(QtCore.QRect(70, 100, 40, 30))
        self.leftAddButton.setObjectName("leftAddButton")
        self.rightAddButton = QtWidgets.QPushButton(XSheetUI)
        self.rightAddButton.setGeometry(QtCore.QRect(130, 100, 40, 30))
        self.rightAddButton.setObjectName("rightAddButton")
        self.example_btn = QtWidgets.QPushButton(XSheetUI)
        self.example_btn.setEnabled(False)
        self.example_btn.setGeometry(QtCore.QRect(30, 10, 31, 31))
        self.example_btn.setText("")
        self.example_btn.setObjectName("example_btn")
        self.delButton = QtWidgets.QPushButton(XSheetUI)
        self.delButton.setGeometry(QtCore.QRect(180, 100, 40, 30))
        self.delButton.setObjectName("delButton")
        self.importBtn = QtWidgets.QPushButton(XSheetUI)
        self.importBtn.setGeometry(QtCore.QRect(10, 100, 61, 30))
        self.importBtn.setObjectName("importBtn")

        self.retranslateUi(XSheetUI)
        QtCore.QMetaObject.connectSlotsByName(XSheetUI)

    def retranslateUi(self, XSheetUI):
        _translate = QtCore.QCoreApplication.translate
        XSheetUI.setWindowTitle(_translate("XSheetUI", "X-Sheet"))
        self.leftButton.setText(_translate("XSheetUI", "<-"))
        self.rightButton.setText(_translate("XSheetUI", "->"))
        self.leftLabel.setText(_translate("XSheetUI", "..."))
        self.rightLabel.setText(_translate("XSheetUI", "..."))
        self.leftAddButton.setText(_translate("XSheetUI", "+"))
        self.rightAddButton.setText(_translate("XSheetUI", "+"))
        self.delButton.setText(_translate("XSheetUI", "-"))
        self.importBtn.setText(_translate("XSheetUI", "Copy..."))
