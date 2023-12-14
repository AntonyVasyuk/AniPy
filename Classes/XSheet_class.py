from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from Tables_Interupting.CSVInterupting import dict_read_from_csv
from UI_Py.XSheet_UI import Ui_XSheetUI

from constants import SPACE, BTN_HEIGHT, BTN_WIDTH

DEP_VIS = "+"
UB_VIS = "*"


class XSheet(QWidget, Ui_XSheetUI):
    def __init__(self, parent_):
        super().__init__()
        self.load_parameters()
        self.setupUi(self)
        self.parent_ = parent_
        # print(self.parent_.x_sheet)

        # self.abandon_visible_frame_indexes = []
        self.depend_visible_frames = [False] * self.num_of_visible_frames

        self.frames = self.parent_.current_project.frames
        # TODO encapsulation fix
        self.choose_index = self.num_of_visible_frames // 2
        self.left_frames_end = 0
        self.right_frames_end = self.num_of_visible_frames - 1
        self.setup_ui_with_features()
        self.update_buttons()
        self.leftButton.clicked.connect(lambda: self.move_visible_frames(-1))
        self.rightButton.clicked.connect(lambda: self.move_visible_frames(1))
        self.leftAddButton.clicked.connect(lambda: self.add_frame(0))
        self.rightAddButton.clicked.connect(lambda: self.add_frame(1))


    def add_frame(self, d):
        self.parent_.current_project.add_frame(self.choose_index + d)
        self.move_visible_frames(not d)
        self.update_buttons()

    def setup_ui_with_features(self):
        self.resize(SPACE * 6 + self.leftButton.width() * 2 + BTN_WIDTH * self.num_of_visible_frames, self.height())
        self.setFixedSize(self.width(), self.height())
        self.rightButton.move(self.width() - self.rightButton.width() - SPACE, self.rightButton.y())
        self.rightLabel.move(self.width() - self.rightButton.width() - SPACE * 3, self.rightButton.y())

        self.example_btn.hide()
        self.frame_buttons = []
        self.visibility_buttons = []
        for i in range(self.num_of_visible_frames):
            btn = QPushButton(self)
            x = self.leftButton.width() + SPACE * 3 + BTN_WIDTH * i
            btn.setGeometry(x, self.leftButton.y(), BTN_WIDTH, BTN_HEIGHT)
            btn.clicked.connect(self.move_cursor_to_mouse)
            self.frame_buttons.append(btn)

            if (i != self.num_of_visible_frames // 2):
                btn = QPushButton(self)
                x = self.leftButton.width() + SPACE * 3 + BTN_WIDTH * i
                btn.setGeometry(x, self.example_btn.y(), BTN_WIDTH, BTN_HEIGHT)
                btn.clicked.connect(self.change_visibility_of_frame)
                self.visibility_buttons.append(btn)
            else:
                self.visibility_buttons.append(QPushButton())

        self.leftAddButton.move(self.frame_buttons[len(self.frame_buttons) // 2 - 1].x(), self.leftAddButton.y())
        self.rightAddButton.move(self.frame_buttons[len(self.frame_buttons) // 2 + 1].x(), self.rightAddButton.y())

    def change_visibility_of_frame(self):
        i = self.visibility_buttons.index(self.sender())
        self.depend_visible_frames[i] = not self.depend_visible_frames[i]
        self.sender().setText("*" * self.depend_visible_frames[i])
        self.move_visible_frames(0)
        self.update_buttons()

    def update_buttons(self):
        for i, btn in enumerate(self.frame_buttons):
            if (0 <= self.left_frames_end + i <= len(self.frames) - 1):
                btn.setEnabled(True)
                btn.setText(str(self.left_frames_end + i + 1))
            else:
                btn.setEnabled(False)
                btn.setText("")

            self.visibility_buttons[i].setEnabled(btn.isEnabled())

            # if (self.frames[self.left_frames_end + i].is_marked):
            #     btn.setText(btn.text() + '*')

        self.leftLabel.setText("" + "..." * self.frame_buttons[0].isEnabled())
        self.rightLabel.setText("" + "..." * self.frame_buttons[-1].isEnabled())

        self.leftButton.setEnabled(self.left_frames_end > -self.num_of_visible_frames // 2 + 1)
        self.rightButton.setEnabled(self.right_frames_end < len(self.frames) + self.num_of_visible_frames // 2 - 1)

        self.leftAddButton.setEnabled(self.frame_buttons[self.num_of_visible_frames // 2].isEnabled())
        self.rightAddButton.setEnabled(self.frame_buttons[self.num_of_visible_frames // 2].isEnabled())

    def move_cursor_to_mouse(self):
        self.move_visible_frames(self.frame_buttons.index(self.sender()) - self.num_of_visible_frames // 2)

    def move_visible_frames(self, d):
        if (self.right_frames_end + d >= self.num_of_visible_frames // 2 and self.left_frames_end + d <= len(self.frames) - 1 - self.num_of_visible_frames // 2):
            self.left_frames_end += d
            self.right_frames_end += d
            self.current_frames = self.frames[self.left_frames_end:self.right_frames_end + 1]
        self.choose_index += d

        new_pixmaps = [None] * self.num_of_visible_frames
        for i in range(self.num_of_visible_frames):
            if (0 <= self.choose_index - self.num_of_visible_frames // 2 + i < len(self.frames)):
                if (self.depend_visible_frames[i]):
                    new_pixmaps[i] = f"{self.frames[self.choose_index - self.num_of_visible_frames // 2 + i].image_path}.png"
                # print(self.choose_index - self.num_of_visible_frames // 2 + i + 1)

        self.parent_.reset_pixmaps(new_pixmaps, f"{self.frames[self.choose_index].image_path}.png")
        self.update_buttons()

    def showEvent(self, event):
        self.load_parameters()
        # self.parent_.show_board_()

    def load_parameters(self):
        settings = dict_read_from_csv("Tables_Interupting/Settings.csv")
        self.num_of_visible_frames = int(settings["NumOfVisibleFrames"])
