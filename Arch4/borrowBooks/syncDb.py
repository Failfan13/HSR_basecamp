import sys
import os
import json
import sqlite3 as sql

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
    for jdict in jsonData:
        sqlData += f'{tuple(jdict.values())}, '
    try:
        connection.execute(
            f'''INSERT OR IGNORE INTO books (isbn, title, author, pages, year)
                VALUES {sqlData[:-2]};'''
        )
    except json.decoder.JSONDecodeError:
        return 'empty file or invalid fields'
