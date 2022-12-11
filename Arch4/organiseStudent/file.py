import sys
import os
import sqlite3 as sql

class studentOrganiser():
    def __init__(self, sqlCon:sql.Connection):
        self.dataBaseInf = 0
        self.sqlCon = sqlCon

    # Function for creating student -> student
    def newStudent(self) -> int:
        stuData = dictQuestions(['first_name', 'last_name', 'city', 'date_of_birth', 'class'])
        self.sqlCon.execute(
            f'''INSERT INTO students {tuple(stuData.keys())}
                VALUES {tuple(stuData.values())}
            '''
        )
        return next(self.sqlCon.execute(
            f'''SELECT studentnumber
                FROM students 
                WHERE first_name = "{stuData.get('first_name')}" 
                AND last_name = "{stuData.get('last_name')}"
                AND date_of_birth = "{stuData.get('date_of_birth')}"
                AND city = "{stuData.get('city')}"
                '''
        ))[0]

    def assignStudent(self) -> None:
        stuData = dictQuestions(['studentnumber', 'class'])
        cur = self.sqlCon.cursor()
        cur.execute(
            f'''SELECT studentnumber from students where studentnumber = "{stuData.get('studentnumber')}"'''
            )
        if cur.fetchall():
            cur.execute(
                f'''UPDATE students
                    SET class = "{stuData.get('class')}"
                    WHERE studentnumber = "{stuData.get('studentnumber')}"'''
            )
        else:
            print(f"invalid student: {stuData.get('studentnumber')}")

    def listStudents(self, classRoom='all') -> None:
        if classRoom == 'all':
            stuData = {'class': 'TRUE', 'order': 'class DESC'}
        else:
            stuData = dictQuestions(["class"])
            stuData['class'] = 'class = "{}"'.format(stuData.get('class'))
            stuData['order'] = 'studentnumber ASC'
        cur = self.sqlCon.cursor()
        cur.execute(
            f'''SELECT * FROM students
                WHERE {stuData.get('class')}
                ORDER BY {stuData.get('order')}'''
        )
        print(cur.fetchall())

    def searchStudent(self) -> None:
        stuData = dictQuestions(['first_name', 'last_name_or_city'])
        cur = self.sqlCon.cursor()
        cur.execute(
            f'''SELECT * FROM students
                WHERE first_name = "{stuData.get('first_name')}" 
                    AND last_name = "{stuData.get('last_name_or_city')}" 
                    OR city = "{stuData.get('last_name_or_city')}"'''
        )
        print(cur.fetchone())


def dictQuestions(questions:list) -> dict:
    return {q:input(q).title() for q in questions}


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
    stuOrg = studentOrganiser(connect)
    while True:
        inp = input(menuStructure.__doc__).upper()
        if inp == 'A':
            stuOrg.newStudent()
        elif inp == 'C':
            stuOrg.assignStudent()
        elif inp == 'D':
            stuOrg.listStudents()
        elif inp == 'L':
            stuOrg.listStudents('other')
        elif inp == 'S':
            stuOrg.searchStudent()
        elif inp == 'Q':
            break
        else:
            print('invalid')
        connect.commit()


if __name__ == "__main__":
    main()