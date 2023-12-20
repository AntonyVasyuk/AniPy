# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AniPy_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AniPyUI(object):
    def setupUi(self, AniPyUI):
        AniPyUI.setObjectName("AniPyUI")
        AniPyUI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AniPyUI)
        self.centralwidget.setObjectName("centralwidget")
        AniPyUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AniPyUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuPanels = QtWidgets.QMenu(self.menubar)
        self.menuPanels.setObjectName("menuPanels")
        self.menuOpen_panel = QtWidgets.QMenu(self.menuPanels)
        self.menuOpen_panel.setObjectName("menuOpen_panel")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        AniPyUI.setMenuBar(self.menubar)
        self.actionX_sheet = QtWidgets.QAction(AniPyUI)
        self.actionX_sheet.setObjectName("actionX_sheet")
        self.actionCreate_project = QtWidgets.QAction(AniPyUI)
        self.actionCreate_project.setObjectName("actionCreate_project")
        self.actionOpen_Project = QtWidgets.QAction(AniPyUI)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionSave_project_as_GIF = QtWidgets.QAction(AniPyUI)
        self.actionSave_project_as_GIF.setObjectName("actionSave_project_as_GIF")
        self.actionTools = QtWidgets.QAction(AniPyUI)
        self.actionTools.setObjectName("actionTools")
        self.menuOpen_panel.addAction(self.actionX_sheet)
        self.menuPanels.addAction(self.menuOpen_panel.menuAction())
        self.menuPanels.addAction(self.actionTools)
        self.menuFile.addAction(self.actionCreate_project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_project_as_GIF)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPanels.menuAction())

        self.retranslateUi(AniPyUI)
        QtCore.QMetaObject.connectSlotsByName(AniPyUI)

    def retranslateUi(self, AniPyUI):
        _translate = QtCore.QCoreApplication.translate
        AniPyUI.setWindowTitle(_translate("AniPyUI", "MainWindow"))
        self.menuPanels.setTitle(_translate("AniPyUI", "Panels"))
        self.menuOpen_panel.setTitle(_translate("AniPyUI", "Open panel..."))
        self.menuFile.setTitle(_translate("AniPyUI", "File"))
        self.actionX_sheet.setText(_translate("AniPyUI", "X-sheet"))
        self.actionCreate_project.setText(_translate("AniPyUI", "Create project"))
        self.actionOpen_Project.setText(_translate("AniPyUI", "Open Project"))
        self.actionSave_project_as_GIF.setText(_translate("AniPyUI", "Save project as GIF"))
        self.actionTools.setText(_translate("AniPyUI", "Tools"))
