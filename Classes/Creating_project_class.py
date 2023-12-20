from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from UI_Py.CreatingProject_UI import *


class CreatingProject(QWidget, Ui_CreatingProject):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setFixedSize(self.width(), self.height())
        self.frame_width.setValue(200)
        self.frame_height.setValue(200)

        self.color = QColor(255, 255, 255)
        self.default_color.setStyleSheet(
            "background-color: {}".format(self.color.name()))

        self.pushButton.clicked.connect(self.create_)
        self.cancel.clicked.connect(self.close_)
        self.default_color.clicked.connect(self.get_default_color)

    def get_default_color(self):
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            self.default_color.setStyleSheet(
                "background-color: {}".format(self.color.name()))

    def close_(self):
        self.parent.creating_project_form = None
        self.close()

    def create_(self):
        self.parent.create_project(**{
            "Name": self.project_name.text(),
            "Width": self.frame_width.value(),
            "Height": self.frame_height.value(),
            "Color": self.color.name()
        })
        self.close()
