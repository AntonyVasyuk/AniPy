from PIL import Image
from PyQt5.QtGui import QImage

from constants import NAME_OF_FOLDER_WITH_FRAMES, SEP
# , NAME_OF_FOLDER_WITH_BACKGROUNDS)


class Frame:
    def __init__(self, parent, is_creating_new=True, is_marked=False, **kwargs):
        # print(kwargs)
        self.parent = parent
        self.number = int(kwargs["Number"])
        self.width = int(kwargs["Width"])
        self.height = int(kwargs["Height"])
        try:
            self.color = kwargs["Color"]
        except KeyError:
            self.color = "#ffffff"
        self.image_path = f"{parent.project_folder}{SEP}{NAME_OF_FOLDER_WITH_FRAMES}{SEP}{self.number}"
        # self.background_path = f"{parent.project_folder}{SEP}{NAME_OF_FOLDER_WITH_BACKGROUNDS}{SEP}{kwargs['Background']}"
        if (is_creating_new):
            PIL_image = Image.new(mode='RGBA', size=(self.width, self.height), color=self.color)
            PIL_image.save(f"{self.image_path}.png")
        self.QT_image = QImage(f"{self.image_path}.png")
        self.is_marked = is_marked
