from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from UI_Py.SavingGif_UI import *

from constants import SEP

class SavingGif(QWidget, Ui_gifSave):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setFixedSize(self.width(), self.height())
        self.saveBtn.clicked.connect(self.save)
        self.one.setChecked(True)
        self.twenty_four.setChecked(True)
        self.inf.setChecked(True)

    def save(self):
        name = self.fileName.text()
        folder = self.get_file_folder()

        name = folder + SEP + name

        # print(name)

        if (self.one.isChecked()):
            on = 1
        if (self.two.isChecked()):
            on = 2
        if (self.three.isChecked()):
            on = 3
        if (self.four.isChecked()):
            on = 4

        if (self.inf.isChecked()):
            loops = 0
        else:
            loops = int(self.loop.text())

        if (self.twenty_four.isChecked()):
            fps = 24
        else:
            fps = 30

        self.parent.save_gif(name, on, loops, fps)

    def get_file_folder(self):
        return QFileDialog.getExistingDirectory(self, "Choose files folder", self.parent.current_project.project_folder
                                                + SEP + "GIF")

    def close_(self):
        self.parent.saving_gif = None
        self.close()
