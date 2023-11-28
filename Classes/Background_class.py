# from PIL import Image
# from PyQt5.QtGui import QImage
#
# from constants import SEP, NAME_OF_FOLDER_WITH_BACKGROUNDS
#
#
# class Background:
#     def __init__(self, parent, is_creating_new=True, **kwargs):
#         # print(kwargs)
#         self.parent = parent
#         self.number = int(kwargs["Number"])
#         self.width = int(kwargs["Width"])
#         self.height = int(kwargs["Height"])
#         self.image_path = f"{parent.project_folder}{SEP}{NAME_OF_FOLDER_WITH_BACKGROUNDS}{SEP}{self.number}"
#
#         if (is_creating_new):
#             self.PIL_image = Image.new(mode='RGBA', size=(self.width, self.height), color=(255, 255, 255, 255))
#             self.PIL_image.save(f"{self.image_path}.png")
#         else:
#             self.PIL_image = Image.open(f"{self.image_path}.png")
#         self.QT_image = QImage(f"{self.image_path}.png")
