# -*- coding: utf-8 -*-


import os
import sqlite3

# from Classes.Background_class import Background
from Classes.Frame_class import Frame
from Tables_Interupting.CSVInterupting import dict_read_from_csv, write_rows_to_csv

from constants import NAME_OF_FOLDER_WITH_FRAMES, SEP, FOLDER_WITH_PROJECTS


class Project:
    def __init__(self, parent, is_creating_new=True, **kwargs):
        self.load_parameters()
        # print(kwargs, '\n')
        self.parent = parent
        self.name = kwargs["Name"]
        self.width = int(kwargs["Width"])
        self.height = int(kwargs["Height"])
        self.color = kwargs["Color"]
        # print(self.color)
        self.frames = []
        # self.backgrounds = []
        self.project_folder = FOLDER_WITH_PROJECTS + f"{SEP}{self.name}"
        self.db_name = f"{self.project_folder}{SEP}{self.name}_db.sqlite"
        if (is_creating_new):
            self.create_dirs()
        else:
            self.con = sqlite3.connect(self.db_name)
            self.cur = self.con.cursor()
            self.import_dirs()


    def import_dirs(self):
        order = [row[0] for row in self.cur.execute("""
        SELECT frame FROM Frames_order
        """)]
        frames = [list(row) for row in self.cur.execute("""
        SELECT * FROM Frames
        """)]
        # print(frames, sep='\n')
        for frame in frames:
            self.frames.append(Frame(self, is_creating_new=False, **{
                "Number": frame[1],
                "Width": frame[2],
                "Height": frame[3],
            }))
        self.last_frame_number = frame[0] - 1





    def create_dirs(self):
        os.mkdir(self.project_folder)

        os.mkdir(f"{self.project_folder}{SEP}{NAME_OF_FOLDER_WITH_FRAMES}")
        self.put_default_frames()

        # os.mkdir(f"{self.project_folder}{SEP}{NAME_OF_FOLDER_WITH_BACKGROUNDS}")
        # self.put_default_background()

        open(self.db_name, mode="w").close()
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE Frames (
            frameId INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            number INTEGER,
            width INTEGER,
            height INTEGER
        );
        """)
        # rotation INTEGER,
        # camera_x INTEGER,
        # camera_y INTEGER,
        # camera_w INTEGER,
        # camera_h INTEGER

        self.con.commit()

        self.cur.execute("""
        CREATE TABLE Frames_order (
            orderId INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            frame INTEGER REFERENCES Frames (frameId)
        );
        """)
        self.con.commit()

        for i in range(len(self.frames)):
            self.cur.execute(f"""
            INSERT INTO Frames(number, width, height)
            VALUES ({self.frames[i].number}, {self.width}, {self.height})
            """)
            self.con.commit()

            self.cur.execute(f"""
            INSERT INTO Frames_order(frame)
            VALUES ({i})
            """)
            self.con.commit()

        open(f"{self.project_folder}{SEP}config.csv", mode="w").close()
        write_rows_to_csv(f"{self.project_folder}{SEP}config.csv", [
            ["Name", self.name],
            ["Width", self.width],
            ["Height", self.height],
            ["Color", self.color]
        ])

    # def put_default_background(self):
    #     self.backgrounds.append(Background(self, **{
    #         "Number": 0,
    #         "Width": self.width,
    #         "Height": self.height
    #     }))

    def put_default_frames(self):
        for i in range(self.num_of_visible_frames):
            self.frames.append(Frame(self, is_marked=True, **{
                "Number": i,
                "Width": self.width,
                "Height": self.height,
                "Color": self.color
                # "Background": 0
            }))
        self.last_frame_number = i

    def load_parameters(self):
        settings = dict_read_from_csv("Tables_Interupting/Settings.csv")
        self.num_of_visible_frames = int(settings["NumOfVisibleFrames"])

    def add_frame(self, i):
        self.frames.insert(i, Frame(self, **{
            "Number": self.last_frame_number + 1,
            "Width": self.width,
            "Height": self.height,
            "Color": self.color
            # "Color": "#ffffff"
            # "Background": 0
        }))
        self.last_frame_number += 1
        self.update_frames()
        self.update_order()

    def update_frames(self):
        self.cur.execute(f"""
        INSERT INTO Frames(number, width, height)
        VALUES ({self.last_frame_number}, {self.width}, {self.height})
        """)
        self.con.commit()

    def update_order(self):
        self.cur.execute("""
        DROP TABLE Frames_order
        """)

        self.cur.execute("""
        CREATE TABLE Frames_order (
            orderId INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            frame INTEGER REFERENCES Frames (frameId)
        )
        """)

        self.con.commit()

        for i in [frame.number for frame in self.frames]:
            self.cur.execute(f"""
            INSERT INTO Frames_order(frame)
            VALUES ({i})
            """)
            self.con.commit()


