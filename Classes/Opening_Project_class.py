import os

from PyQt5.QtWidgets import *

from Tables_Interupting.CSVInterupting import list_read_from_csv, dict_read_from_csv
from UI_Py.OpeningProject_UI import *

from constants import FOLDER_WITH_PROJECTS, SEP


class OpeningProject(QWidget, Ui_OpenProject):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.projects_names = os.listdir(FOLDER_WITH_PROJECTS)
        # print(self.projects_names)
        # print(*self.projects_names)
        self.projects_to_open.insertItems(0, self.projects_names)
        self.open.clicked.connect(self.open_project)
        self.cancel.clicked.connect(self.close_)

    def close_(self):
        self.parent.opening_project_form = None
        self.close()

    def open_project(self):
        params = dict_read_from_csv(f"{FOLDER_WITH_PROJECTS}{SEP}{self.projects_to_open.currentText()}{SEP}config.csv")
        self.parent.open_project(**params)
        self.close()