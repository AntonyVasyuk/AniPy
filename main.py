import os
import sys

from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Classes.Creating_project_class import CreatingProject
from Classes.Opening_Project_class import OpeningProject
from Classes.SavingGif_class import SavingGif
from Classes.Tools_class import Tools
from Classes.XSheet_class import XSheet
from UI_Py.AniPy_UI import Ui_AniPyUI
from Classes.Project_class import Project
from constants import FOLDER_WITH_PROJECTS


class Brush:  # Class of brush, that draw via given painter
    def __init__(self, x, y, painter: QPainter):
        self.name = "brush"
        self.x = x
        self.y = y
        self.painter = painter

    def draw(self, size):
        self.painter.drawEllipse(QPoint(self.x, self.y), size, size)


class AniPy(QMainWindow, Ui_AniPyUI):  # Main program class, foundation of a-a-a-all the things
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.num_of_visible_frames = 11

        # All about drawing
        self.paint = False
        self.objects_to_paint = []
        self.draw_mode = "brush"
        self.brush_size = 5
        self.color = "#000000"
        self.main_color = "#000000"
        self.second_color = "#ffffff"

        # Forms
        self.tools = None
        self.x_sheet = None
        self.creating_project_form = None
        self.opening_project_form = None
        self.current_project = None
        self.saving_gif = None

        # Connections
        self.menuFile.aboutToShow.connect(self.check_menus)
        self.actionX_sheet.triggered.connect(self.show_x_sheet)
        self.actionCreate_project.triggered.connect(self.get_new_project_params)
        self.actionOpen_Project.triggered.connect(self.what_project_to_open)
        self.actionSave_project_as_GIF.triggered.connect(self.get_saving_gif_params)
        self.actionTools.triggered.connect(self.show_tools)

    def save_gif(self, *args):  # Saving to GIF current project
        file_name, on_what, num_of_loops, fps = args
        for_gif = []
        for frame in self.current_project.frames:
            image = Image.open(f"{frame.image_path}.png")
            for i in range(on_what):
                for_gif.append(image)

        frame_0 = for_gif[0]
        del for_gif[0]
        d = int((1 / fps) * 1000)
        frame_0.save(f"{file_name}.gif", save_all=True, append_images=for_gif, optimize=False, loop=num_of_loops,
                     duration=d)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if (event.button() == Qt.LeftButton):
            self.color = self.main_color
        else:
            self.color = self.second_color

        if (self.current_project is not None):
            if (self.board.x() <= event.x() <= self.board.x() + self.board.width() and
                    self.board.y() <= event.y() <= self.board.y() + self.board.height()):
                self.mouse_x = event.x() - self.board.x()
                self.mouse_y = event.y() - self.board.y()
                self.objects_to_paint.append(self.what_object_to_draw())
                self.paint = True
                self.was_out_of_board = False
                self.update()
            else:
                self.was_out_of_board = True

    def what_object_to_draw(self, x=None, y=None):
        if (x is None):
            x = self.mouse_x
        if (y is None):
            y = self.mouse_y
        match self.draw_mode:
            case "brush":
                return Brush(x, y, self.painter)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if (self.paint):
            if (self.current_project is not None):
                if (self.board.x() <= event.x() <= self.board.x() + self.board.width() and
                        self.board.y() <= event.y() <= self.board.y() + self.board.height()):

                    self.mouse_x = event.x() - self.board.x()
                    self.mouse_y = event.y() - self.board.y()
                    prev_mouse_x = self.objects_to_paint[-1].x
                    prev_mouse_y = self.objects_to_paint[-1].y
                    if (not self.was_out_of_board):
                        n = 10
                        for i in range(1, n):
                            self.objects_to_paint.append(self.what_object_to_draw(
                                prev_mouse_x + i * (self.mouse_x - prev_mouse_x) // n,
                                prev_mouse_y + i * (self.mouse_y - prev_mouse_y) // n
                            ))
                    self.was_out_of_board = False
                    self.objects_to_paint.append(self.what_object_to_draw())
                else:
                    self.was_out_of_board = True

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if (self.paint):
            self.paint = False
            self.objects_to_paint.clear()
            self.pixmap.save(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")
            pil_image = Image.open(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")
            data = list(pil_image.getdata())
            new_image = Image.new(mode="RGBA", size=(self.pixmap.width(), self.pixmap.height()))
            new_image.putdata(data)
            new_image.save(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if (self.paint):
            self.painter.setPen(QColor(self.color))
            self.painter.setBrush(QColor(self.color))

            for obj in self.objects_to_paint:
                match obj.name:
                    case "brush":
                        obj.draw(self.brush_size)

            self.reset_pixmap(self.pixmap)

    def check_menus(self):
        if (os.listdir(FOLDER_WITH_PROJECTS)):
            self.actionOpen_Project.setEnabled(True)
        else:
            self.actionOpen_Project.setEnabled(False)

    def get_saving_gif_params(self):
        if (self.saving_gif is None):
            self.saving_gif = SavingGif(self)
        self.saving_gif.show()

    def show_tools(self):
        if (self.tools is None):
            self.tools = Tools(self)
        self.tools.show()

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
        self.show_board()
        self.show_tools()

    def create_project(self, **kwargs):
        self.creating_project_form = None
        self.current_project = Project(self, **kwargs)
        self.actionX_sheet.trigger()
        self.show_board()
        self.show_tools()

    def reset_pixmap(self, pixmap):
        self.painter.end()
        self.pixmap = pixmap
        self.board.setPixmap(self.pixmap)
        self.painter.begin(self.pixmap)

    def reset_pixmaps(self, paths, path):
        self.painter.end()
        self.pixmap = QPixmap(path)
        self.pixmap_path = path
        self.board.setPixmap(self.pixmap)
        self.painter.begin(self.pixmap)

        self.pixmap_paths = paths
        for i, path in enumerate(self.pixmap_paths):
            if (path is not None):
                self.pixmaps[i] = QPixmap(path)
            else:
                self.pixmaps[i] = None

        for i in range(len(self.boards)):
            if (i != self.num_of_visible_frames // 2):
                if (self.pixmaps[i] is not None):
                    self.pixmaps[i] = return_transparent_pixmap(
                        self.pixmap_paths[i], 0.1 * abs(self.num_of_visible_frames // 2 - i)
                    )

                    self.boards[i].show()
                    self.boards[i].setPixmap(self.pixmaps[i])
                else:
                    self.boards[i].hide()

    def show_board(self):
        self.board = QLabel(self)
        self.board.setGeometry(10, 30, self.current_project.width, self.current_project.height)
        self.board.show()
        self.pixmap = QPixmap(f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")
        self.board.setPixmap(self.pixmap)

        self.pixmaps = [None] * self.num_of_visible_frames
        self.boards = [None] * self.num_of_visible_frames

        self.painter = QPainter(self.pixmap)
        self.painter.begin(self.pixmap)

        for i in range(len(self.boards)):
            if (i != self.num_of_visible_frames // 2):
                self.boards[i] = QLabel(self)
                self.boards[i].setGeometry(10, 30, self.current_project.width, self.current_project.height)

        self.reset_pixmaps(self.pixmaps, f"{self.x_sheet.frames[self.x_sheet.choose_index].image_path}.png")

    # def return_transparent_pixmap_legacy(self, path, t):
    #     t = int(t * 255)
    #
    #     print(t)
    #     image = QImage(path)
    #     for i in range(image.height()):
    #         for j in range(image.width()):
    #             # image.pixel(j, i)
    #             # image.setPixel(j, i, QColor())
    #
    #             rgb = QColor(image.pixel(j, i))
    #             r, g, b, a = rgb.getRgb()
    #             # print(r, g, b, a)
    #             image.setPixelColor(QPoint(j, i), QColor(r, g, b, t))
    #
    #     pixmap = QPixmap(image)
    #     return pixmap
    #
    # Little note: if I did the transparency with this method, adding of opacity will be very long, so I did it with
    # the next function, that works with bless of some magic functions


def return_transparent_pixmap(path, t):
    pixmap = QPixmap(path)
    image = QImage(path)
    painter = QPainter(image)

    image.fill(Qt.transparent)

    painter.begin(image)

    painter.setOpacity(t)
    painter.drawPixmap(0, 0, pixmap)

    painter.end()

    return QPixmap(image)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AniPy()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
