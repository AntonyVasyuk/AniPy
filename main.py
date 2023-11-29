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


class Brush:
    def __init__(self, x, y, size, painter: QPainter):
        self.name = "brush"
        self.x = x
        self.y = y
        self.size = size
        self.painter = painter

    def draw(self):
        self.painter.drawEllipse(QPoint(self.x, self.y), self.size, self.size)



class AniPy(QMainWindow, Ui_AniPyUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_settings_to_default()
        # self.
        # self.styleSheet()
        # print(self.styleSheet())
        self.paint = False
        self.objects_to_paint = []
        self.draw_mode = "brush"
        self.brush_size = 5
        self.x_sheet = None
        self.creating_project_form = None
        self.opening_project_form = None
        self.current_project = None
        self.menuFile.aboutToShow.connect(self.check_menus)
        self.actionX_sheet.triggered.connect(self.show_x_sheet)
        self.actionCreate_project.triggered.connect(self.get_new_project_params)
        self.actionOpen_Project.triggered.connect(self.what_project_to_open)
        self.setMouseTracking(True)

        # self.painter = QPainter(self.board)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if (self.current_project is not None):
            if (self.board.x() <= event.x() <= self.board.x() + self.board.width() and
                    self.board.y() <= event.y() <= self.board.y() + self.board.height()):
                self.mouse_x = event.x() - self.board.x()
                self.mouse_y = event.y() - self.board.y()
                self.objects_to_paint.append(self.what_object_to_draw())
                self.paint = True
                self.paintEvent(QPaintEvent(QRegion()))

    def what_object_to_draw(self):
        match self.draw_mode:
            case "brush":
                return Brush(self.mouse_x, self.mouse_y, self.brush_size, self.painter)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if (self.paint):
            if (self.current_project is not None):
                if (self.board.x() <= event.x() <= self.board.x() + self.board.width() and
                        self.board.y() <= event.y() <= self.board.y() + self.board.height()):
                    self.mouse_x = event.x() - self.board.x()
                    self.mouse_y = event.y() - self.board.y()
                    self.objects_to_paint.append(self.what_object_to_draw())

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.paint = False
        self.painter.end()
        self.pixmap.save(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if (self.paint):
            print('!')
            self.painter.begin(self.pixmap)
            self.painter.setPen(QColor(0, 0, 0))
            self.painter.setBrush(QColor(0, 0, 0))
            # self.painter.drawPoint(self.mouse_x, self.mouse_y)

            for obj in self.objects_to_paint:
                match obj.name:
                    case "brush":
                        obj.draw()
                        del self.objects_to_paint[-1]

            self.reset_pixmap(self.pixmap)
        # self.paint = False

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
        self.actionX_sheet.trigger()
        self.show_board()

    def show_board_(self):
        self.show_board()

    def reset_pixmap(self, pixmap):
        self.pixmap = pixmap
        self.board.setPixmap(self.pixmap)

    def show_board(self):
        # self.setFocus()
        self.board = QLabel(self)
        self.board.setGeometry(10, 30, self.current_project.width, self.current_project.height)
        self.board.show()
        self.pixmap = QPixmap(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")
        self.board.setPixmap(self.pixmap)

        self.painter = QPainter(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AniPy()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())