import os
import sys

import csv

from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Classes.Creating_project_class import CreatingProject
from Classes.Opening_Project_class import OpeningProject
from Tables_Interupting.CSVInterupting import write_rows_to_csv, list_read_from_csv
from Classes.XSheet_class import XSheet
from UI_Py.AniPy_UI import Ui_AniPyUI
from Classes.Project_class import Project
from constants import FOLDER_WITH_PROJECTS


class AniPy(QMainWindow, Ui_AniPyUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_settings_to_default()
        # self.
        # self.styleSheet()
        # print(self.styleSheet())
        self.x_sheet = None
        self.creating_project_form = None
        self.opening_project_form = None
        self.menuFile.aboutToShow.connect(self.check_menus)
        self.actionX_sheet.triggered.connect(self.show_x_sheet)
        self.actionCreate_project.triggered.connect(self.get_new_project_params)
        self.actionOpen_Project.triggered.connect(self.what_project_to_open)


        # self.painter = QPainter()

        # self.board = QLabel(self)
        # self.board.setGeometry(0, 0, 0, 0)
        # self.pixmap = None
        # self.show_board()
        # self.actionX_sheet.trigger()

    # def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
    #     print(0)
    #     self.update()
    #
    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     self.painter.begin(self)
    #     self.painter.setBrush(QColor("#ffffff"))
    #     self.painter.setPen(QColor("#ffffff"))
    #
    #
    #     self.painter.drawEllipse(10, 10, 100, 100)
    #     print(0)
    #
    #     self.painter.end()
    #     # self.update()

    def check_menus(self):
        if (os.listdir(FOLDER_WITH_PROJECTS)):
            self.actionOpen_Project.setEnabled(True)
        else:
            self.actionOpen_Project.setEnabled(False)

    def set_settings_to_default(self):
        rows = list_read_from_csv('Tables_Interupting/Default_Settings.csv')
        write_rows_to_csv("Tables_Interupting/Settings.csv", rows)

    def show_x_sheet(self):
        if (self.x_sheet is None):
            self.x_sheet = XSheet(self)
        self.x_sheet.show()

    def get_new_project_params(self):
        if (self.creating_project_form is None):
            self.creating_project_form = CreatingProject(self)
        self.creating_project_form.show()

    def what_project_to_open(self):
        if (self.opening_project_form is None):
            self.opening_project_form = OpeningProject(self)
        self.opening_project_form.show()

    def open_project(self, **kwargs):
        self.opening_project_form = None
        self.current_project = Project(self, is_creating_new=False, **kwargs)
        self.actionX_sheet.trigger()

    def create_project(self, **kwargs):
        self.creating_project_form = None
        self.current_project = Project(self, **kwargs)
        # self.x_sheet = XSheet(self)
        # self.x_sheet.show()
        self.actionX_sheet.trigger()
        self.show_board()

    def show_board_(self):
        self.show_board()

    def reset_pixmap(self, pixmap):
        self.pixmap = pixmap
        self.board.setPixmap(self.pixmap)

    def show_board(self):
        # print(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png", self.current_project.width, sep='\n')

        # self.board = Board(self)
        # self.board.setParent(self)
        #
        # self.board.setGeometry(10, 30, self.current_project.width, self.current_project.height)
        # self.pixmap = QPixmap(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")
        # self.board.setPixmap(self.pixmap)

        self.setFocus()
        self.board = QLabel(self)
        self.board.setGeometry(10, 30, self.current_project.width, self.current_project.height)
        # self.board.setGeometry(10, 30, 100, 100)
        # self.board.setText("Hello!!!11!")
        self.board.show()
        self.pixmap = QPixmap(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")
        # self.pixmap = QPixmap(r"C:\Users\vasyu\OneDrive\Рабочий стол\Untitled.png")
        # print(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")
        self.board.setPixmap(self.pixmap)
        # print(000)


        # self.board.setText("Hello!")
        # self.update()
        # print(self.board.pixmap())

    # def paint_point(self, event: QtGui.QMouseEvent):
        # self.painter.begin(self.board.pixmap())
        #
        # self.painter.setBrush(QColor(0, 0, 255, 255))
        # self.painter.drawPoint(event.x(), event.y())
        #
        # self.painter.end()


# class Board(QLabel):
#     def __init__(self, parent):
#         super(Board, self).__init__()
#         self.parent = parent
#
#         self.painter = QPainter()
#
#         self.mouse_cords = [0, 0]
#         # self.board = QLabel(self)
#         # self.board.setGeometry(0, 0, self.width(), self.height())
#         # self.pixmap = QPixmap(f"{self.parent.x_sheet.frames[self.parent.x_sheet.choose_index].image_path}.png")
#         # self.setPixmap(self.pixmap)
#         # self.painter = QPainter(self.pixmap)
#
#     def mousePressEvent(self, event: QMouseEvent):
#         print(9)
#         self.mouse_cords = [event.x(), event.y()]
#         self.update()
#         # self.parent.paint_point(event)
#
#     def paintEvent(self, a0):
#         self.painter.begin(self.pixmap())
#
#         self.painter.setBrush(QColor("#ffffff"))
#         self.painter.setPen(QColor("#000000"))
#         self.painter.drawEllipse(self.mouse_cords[0], self.mouse_cords[1], 10, 10)
#         self.update()
#
#         self.painter.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AniPy()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())