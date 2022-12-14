import sys
import os
import json
import sqlite3 as sql
from datetime import datetime as dt, timedelta

class bookStoreAp():
    def __init__ (self, connection:sql.Connection):
        self.con = connection
        self.date = dt.now()

    def borrowBook(self) -> str:
        question = askQuestion(['id_or_isbn', 'duration'])
        self.con.execute(
            f'''SELECT id, title, isbn, status
                FROM books
                WHERE id= "{question.get('id_or_isbn')}" AND status = "AVAILABLE" 
                    OR isbn = "{question.get('id_or_isbn')}" AND status = "AVAILABLE" 
                    '''
        )
        dataOneRow = self.con.fetchone()
        if dataOneRow:
            returnDate = self.date.date() + timedelta(days=int(question.get('duration')))
            self.con.execute(
                '''UPDATE books
                    SET status = "BORROWED", return_date = "{}"
                    WHERE id = "{}"'''.format(strDate(returnDate, 'f'), dataOneRow[0])
            )
            return strDate(returnDate, 'f')
        else:
            return 'Book has been borrowed or is not available'

    def returnBook(self, fee=0.5):
        question = askQuestion(['id_or_isbn'])
        self.con.execute(
            '''SELECT id, return_date
                FROM books
                WHERE id = "{}" AND status = "BORROWED" 
                    OR isbn = {} AND status = "BORROWED"
                '''.format(question.get('id_or_isbn'), question.get('id_or_isbn'))
        )
        dataOneRow = self.con.fetchone()
        if dataOneRow:
            self.con.execute(
                    '''UPDATE books
                        SET status = "AVAILABLE", return_date = 'NULL'
                        WHERE id = "{}"
                        '''.format(dataOneRow[0])
                )
            overDue = (self.date - strDate(dataOneRow[1], 'p')).days
            if overDue > 0:
                return '{:.2f}'.format(overDue * fee)
            else:
                return 'Returned in time'
        else:
            return 'This book has not been borrowed'

    def searchBook(self):
        question = askQuestion(['searchterm'])
        terms = ['id', 'isbn', 'title', 'author', 'pages', 'year', 'status', 'return_date']
        self.con.execute(
            '''SELECT *
                FROM books
                WHERE title = "{}" OR isbn = "{}" OR author = "{}"
                '''.format(question.get('searchterm'), 
                    question.get('searchterm'), question.get('searchterm'))
        )
        selfData = list(self.con.fetchone())
        if selfData[-1] == 'NULL':
            selfData.pop()
            selfData.append(None)
        return dict(zip(terms, selfData))


# Load existing from json if there is any
def readJson():
    try:
        with open(os.path.join(sys.path[0], 'books.json'), mode='r') as jsonFile:
            data = json.load(jsonFile)
            return data
    except FileNotFoundError:
        return []


# Create a sql execution to insert all values from JSON
def syncJsonDb(connection:sql.Connection):
    jsonData = readJson()
    sqlData = ''
    isbns = set([row[0] for row in connection.execute("SELECT isbn FROM books;").fetchall()])
    for jdict in jsonData:
        if jdict.get('isbn') not in isbns:
            sqlData += f'{tuple(jdict.values())}, '
    try:
        if sqlData != '':
            connection.execute(
                f'''INSERT INTO books (isbn, title, author, pages, year)
                    VALUES {sqlData[:-2]};'''
            )
        else:
            pass
    except json.decoder.JSONDecodeError:
        return 'empty file or invalid fields'


# Question to be asked the user
def askQuestion(lstQuest:list):
    return {q: input(q) for q in lstQuest}


def strDate(inputDate, inp:str):
    if inp.lower() == 'f':
        return dt.strftime(inputDate, '%d-%m-%Y')
    else:
        return dt.strptime(inputDate, '%d-%m-%Y')


def menuStructure():
    """[B] Borrow book
[R] Return book
[S] Search book
[Q] Quit"""


def main():
    connect = sql.connect(os.path.join(sys.path[0], 'bookstore.db'))
    connect.execute(
        '''CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL)
        '''
    )
    con = connect.cursor()
    syncJsonDb(con)
    bs = bookStoreAp(con)
    while True:
        inp = input(menuStructure.__doc__).upper()
        if inp == 'B':
            print(bs.borrowBook())
        elif inp == 'R':
            print(bs.returnBook())
        elif inp == 'S':
            print(bs.searchBook())
        elif inp == 'Q':
            break
        else:
            print('invalid')
    connect.commit()

if __name__ == "__main__":
    main()