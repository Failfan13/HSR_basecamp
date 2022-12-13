import sys
import os
import json
import math
import sqlite3 as sql
from datetime import datetime as dt, timedelta


class bookStoreAp():
    def __init__ (self, connection:sql.Connection):
        self.con = connection

    def borrowBook(self):
        question = askQuestion(['id_or_isbn', 'duration'])
        # check if status is availible based on title or isbn
        # return date until = current date + timedelta "question" duration

    def returnBook(self):
        question = askQuestion(['id_or_isbn'])
        # fine if returned later return_date (0.5eu per day)

    def searchBook(self):
        question = askQuestion(['searchterm']) # can be title, isbn or author
        # return book info + status_information (can be AVAILIBLE or BORROWED)

# Question to be asked the user
def askQuestion(lstQuest:list):
    return {q: input(q) for q in lstQuest}

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
    insInto = ''
    for jdict in jsonData:
        if 'status' in jdict.keys():
            insInto = '(isbn, title, authors, pages, year, status, return_date)'
        else:
            insInto = '(isbn, title, authors, pages, year)'
        sqlData += f'{tuple(jdict.values())}, '
    try:
        connection.execute(
            f'''INSERT INTO books {insInto}
                VALUES {sqlData[:-2]};'''
        )
    except json.decoder.JSONDecodeError:
        return 'empty file or invalid fields'


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
            authors TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        )'''
    )
    con = connect.cursor()
    syncJsonDb(con)
    bs = bookStoreAp(con)
    bs.borrowBook()
    connect.commit()
    # bookStore = bookStoreAp(connect)
    # bookStore.borrowBook()
    # connect.commit()
    # while True:
    #     inp = input(menuStructure.__doc__).upper()
    #     if inp == 'B':
    #         borrowBook()
    #     elif inp == 'R':
    #         ...
    #     elif inp == 'S':
    #         ...
    #     elif inp == 'Q':
    #         break
    #     else:
    #         print('invalid')

if __name__ == "__main__":
    main()