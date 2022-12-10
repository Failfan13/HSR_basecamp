import sys
import os
import json
import math
import sqlite3 as sql

class studentOrganiser():
    def __init__(self):
        self.dataBaseInf = 0

    # Function for creating student -> student
    def newStudent():
        ...

    def searchAssignStudent():
        ...

    # List all students > no class given = all -> class descOrd, with class is in that classroom -> stNr asOrd 
    def listStudents(classRoom='all'):
        ...

def menuStructure():
    """[A] Add new student
[C] Assign student to class
[D] List all students
[L] List all students in class
[S] Search student
[Q] Quit"""


def main():
    connect = sql.connect(os.path.join(sys.path[0], 'studentdatabase.db'))
    connect.execute(
        '''CREATE TABLE IF NOT EXISTS students (
            studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            class TEXT DEFAULT NULL 
        );'''
    )
    # while True:
    #     inp = input(menuStructure.__doc__).upper()
    #     if inp == 'A':
    #         ...
    #     elif inp == 'C':
    #         ...
    #     elif inp == 'D':
    #         ...
    #     elif inp == 'L':
    #         ...
    #     elif inp == 'S':
    #         ...
    #     elif inp == 'Q':
    #         ...
    #     else:
    #         print('invalid')
    #     break


if __name__ == "__main__":
    print(main().__doc__)