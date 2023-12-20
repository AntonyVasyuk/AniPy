# -*- coding: utf-8 -*-


import os
import sqlite3

from Classes.Frame_class import Frame
from CSVInterupting import write_rows_to_csv

from constants import NAME_OF_FOLDER_WITH_FRAMES, SEP, FOLDER_WITH_PROJECTS


class Project:
    def __init__(self, parent, is_creating_new=True, **kwargs):
        self.parent = parent
        self.num_of_visible_frames = self.parent.num_of_visible_frames
        self.name = kwargs["Name"]
        self.width = int(kwargs["Width"])
        self.height = int(kwargs["Height"])
        self.color = kwargs["Color"]

        self.frames = []

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
        for i in order:
            self.frames.append(Frame(self, is_creating_new=False, **{
                "Number": i,
                "Width": self.width,
                "Height": self.height,
            }))

    def create_dirs(self):
        os.mkdir(self.project_folder)

        os.mkdir(f"{self.project_folder}{SEP}{NAME_OF_FOLDER_WITH_FRAMES}")
        os.mkdir(f"{self.project_folder}{SEP}GIF")
        self.put_default_frames()

        open(self.db_name, mode="w").close()
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE Frames_order (
            orderId INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            frame INTEGER REFERENCES Frames (frameId)
        );
        """)
        self.con.commit()

        for i in range(len(self.frames)):
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

    def put_default_frames(self):
        for i in range(self.num_of_visible_frames):
            self.frames.append(Frame(self, is_marked=True, **{
                "Number": i,
                "Width": self.width,
                "Height": self.height,
                "Color": self.color
            }))

    def add_frame(self, i):
        last = self.cur.execute(f"""
        SELECT orderId FROM Frames_order
        """).fetchall()[-1][0]
        self.frames.insert(i, Frame(self, **{
            "Number": last,
            "Width": self.width,
            "Height": self.height,
            "Color": self.color
        }))
        self.update_order()

    def del_frame(self, i):
        del self.frames[i]
        self.update_order()

    def del_frame_from_sql(self, i):
        self.cur.execute(f"""
        DELETE FROM Frames_order
        WHERE orderId = {i - 1}
        """)

    def update_order(self):
        self.cur.execute("""
        DROP TABLE Frames_order
        """)
        self.con.commit()

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
