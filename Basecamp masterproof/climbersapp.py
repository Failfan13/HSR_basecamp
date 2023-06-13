import os
import sys
import json
import sqlite3 as sql

from datetime import datetime
from climber import Climber
from mountain import Mountain
from expedition import Expedition
from db_helper import SQL_helper

class Expedition_database:

    def __init__(self, json_file_name:str, db_file_name:str) -> None:
        self.json_file_name = json_file_name
        self.json_content = load_json(self.json_file_name)
        self.executor = SQL_helper(db_file_name)
        self.executor.execute_query(
            """CREATE TABLE IF NOT EXISTS climbers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                nationality TEXT NOT NULL,
                date_of_birth DATE NOT NULL
            );CREATE TABLE IF NOT EXISTS expedition_climbers (
                climber_id INTEGER NOT NULL,
                expedition_id INTEGER NOT NULL,
                PRIMARY KEY(climber_id, expedition_id)
            );CREATE TABLE IF NOT EXISTS mountains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country TEXT NOT NULL,
                rank INTEGER NOT NULL,
                height INTEGER NOT NULL,
                prominence INTEGER NOT NULL,
                range TEXT
            );CREATE TABLE IF NOT EXISTS expeditions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                mountain_id INTEGER NOT NULL,
                start_location TEXT NOT NULL,
                date DATE NOT NULL,
                country TEXT NOT NULL,
                duration INTEGER NOT NULL,
                success BOOLEAN DEFAULT FALSE
            );"""
        )
        sync_json_database(self.json_content, self.executor)
        print(Climber(85, 'Merrily', 'Gyles', 'Pakistan', datetime(1904, 11, 6).date()).get_expeditions())

 
def sync_json_database(json_content:list, sql_func:object) -> None:
    for expedition in json_content:
        # Climbers from expedition:list foreach insert into db
        for climber in expedition.get('climbers'):
            climber['date_of_birth'] = datetime.strptime(climber.get('date_of_birth'), '%d-%m-%Y').date() # too long
            climber = Climber(**climber).__dict__
            climber['date_of_birth'] = str(climber.get('date_of_birth'))
            sql_func.execute_query('''INSERT OR IGNORE INTO climbers {} VALUES {}'''.format(
                tuple(climber.keys()), tuple(climber.values())))
            # Connect climber id to expedition id
            sql_func.execute_query('''INSERT OR IGNORE INTO expedition_climbers (climber_id,
                expedition_id) VALUES (?,?)''', [climber.get('id'), expedition.get('id')])
        # Mountain from expedition & insert into db
        mountain = Mountain(**expedition.get('mountain')).__dict__
        mountain['country'] = mountain.get('country')[0]
        sql_func.execute_query('''INSERT INTO mountains {} SELECT :name, :country, :rank,
            :height, :prominence, :range
                WHERE NOT EXISTS(SELECT 1 FROM mountains WHERE name = "{}")'''.format(
                    tuple(mountain.keys()), mountain.get('name')), mountain)
        # Request mountain id, pop what not needed & change start to start_location
        expedition['mountain_id'] = sql_func.execute_query('''SELECT id FROM mountains
            WHERE name = ?''', [expedition.get('mountain').get('name')], fetch='one')
        expedition.pop('mountain')
        expedition.pop('climbers')
        expedition = Expedition(**expedition).__dict__
        expedition['start_location'] = expedition.pop('start')
        sql_func.execute_query('''INSERT OR IGNORE INTO expeditions {}
           VALUES {}'''.format(tuple(expedition.keys()), tuple(expedition.values())))


def load_json(content:str) -> list:
    try:
        with open(os.path.join(sys.path[0], content + '.json'), mode='r', encoding='UTF-8'
        ) as jContent: return json.load(jContent)
    except FileNotFoundError:
        print('Invalid file')


def main(json_file_name:str, db_file_name:str):
    Expedition_database(json_file_name, db_file_name)


if __name__ == "__main__":
    json_file_name = 'expeditions'
    db_file_name = 'climbersapp'
    main(json_file_name, db_file_name)