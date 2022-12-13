import sys
import os
import sqlite3 as sql
from datetime import datetime as dt, timedelta
from syncDb import syncJsonDb


class bookStoreAp():
    def __init__ (self, connection:sql.Connection):
        self.con = connection
        self.date = dt.now()

    def borrowBook(self):
        question = askQuestion(['id_or_isbn', 'duration'])
        self.con.execute(
            f'''SELECT id, title, isbn, status
                FROM books
                WHERE id= "{question.get('id_or_isbn')} AND status = "AVAILABLE" 
                    OR isbn = "{question.get('id_or_isbn')}" AND status = "AVAILABLE" 
                    '''
        )
        dataOneRow = self.con.fetchone()
        if dataOneRow:
            returnDate = self.date.date() + timedelta(days=int(question.get('duration')))
            self.con.execute(
                '''UPDATE books
                    SET status = "BORROWED", return_date = "{}"
                    WHERE id = "{}"'''.format(returnDate, dataOneRow[0])
            )
            return returnDate
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
                        SET status = "AVAILABLE", return_date = "NULL"
                        WHERE id = "{}"
                        '''.format(dataOneRow[0])
                )
            overDue = (self.date - dt.strptime(dataOneRow[1], "%Y-%m-%d")).days
            if overDue > 0:
                return overDue * fee
            else:
                return 'Returned in time'
        else:
            return 'This book has not been borrowed'

    def searchBook(self):
        question = askQuestion(['searchterm']) # can be title, isbn or author
        self.con.execute(
            '''SELECT isbn, title, pages, year, status
                FROM books
                WHERE title = "{}" OR isbn = "{}" OR author = "{}"
                '''.format(question.get('searchterm'), 
                    question.get('searchterm'), question.get('searchterm'))
        )
        return self.con.fetchone()

# Question to be asked the user
def askQuestion(lstQuest:list):
    return {q: input(q) for q in lstQuest}

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
            return_date DATE DEFAULT NULL,
            UNIQUE(title, isbn)
        )'''
    )
    con = connect.cursor()
    syncJsonDb(con)
    bs = bookStoreAp(con)
    while True:
        inp = input(menuStructure.__doc__).upper()
        if inp == 'B':
            bs.borrowBook()
        elif inp == 'R':
            bs.returnBook()
        elif inp == 'S':
            bs.searchBook()
        elif inp == 'Q':
            break
        else:
            print('invalid')
    connect.commit()

if __name__ == "__main__":
    main()