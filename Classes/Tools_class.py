from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *

from UI_Py.Tools_UI import Ui_UI_Tools


class Tools(QWidget, Ui_UI_Tools):
    def __init__(self, parent_):
        super().__init__()
        self.setupUi(self)
        self.parent_ = parent_
        self.setFixedSize(self.width(), self.height())
        self.move(self.parent_.x() + self.parent_.width() + 10, self.parent_.y())

        self.isFillBtn.hide()

        self.p = QPainter()
        self.p.begin(self)
        self.p.setBrush(QColor(0, 0, 0))
        self.p.setPen(QColor(0, 0, 0))

        self.lmb_color = "#000000"
        self.rmb_color = "#ffffff"
        self.lmbBtn.clicked.connect(self.get_color)
        self.rmbBtn.clicked.connect(self.get_color)
        self.swapBtn.clicked.connect(self.swap_colors)

        self.lineThick.setMinimum(1)
        self.lineThick.setMaximum(20)
        self.lineThick.setSingleStep(1)
        self.lineThick.setValue(5)

        self.lineSize.setMinimum(1)
        self.lineSize.setMaximum(20)
        self.lineSize.setValue(5)

        self.lineSize.valueChanged.connect(self.update_line)
        self.lineThick.valueChanged.connect(self.update_line)

        self.lmbBtn.setStyleSheet(
            "background-color: {}".format(self.lmb_color))
        self.rmbBtn.setStyleSheet(
            "background-color: {}".format(self.rmb_color))

    def swap_colors(self):
        self.lmb_color, self.rmb_color = self.rmb_color, self.lmb_color
        self.update_colors()

    def update_line(self):
        if (self.sender() == self.lineSize):
            self.lineThick.setValue(self.lineSize.value())
        else:
            self.lineSize.setValue(self.lineThick.value())
        self.parent_.brush_size = self.lineSize.value()

    def get_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            if (self.sender() == self.lmbBtn):
                self.lmb_color = color.name()
            else:
                self.rmb_color = color.name()
        self.update_colors()

    def update_colors(self):
        self.parent_.main_color = self.lmb_color
        self.parent_.second_color = self.rmb_color
        self.lmbBtn.setStyleSheet(
            "background-color: {}".format(self.lmb_color))
        self.rmbBtn.setStyleSheet(
            "background-color: {}".format(self.rmb_color))
