import sqlite3 as sql
from db_helper import SQL_helper

class Mountain:

    def __init__(self, name:str, countries:str, rank:int, height:int, prominence:int, range:str, id:int=0) -> None:
        if not id == 0:
            self.id = id
        self.name = name
        self.country = countries
        self.rank = rank
        self.height = height
        self.prominence = prominence
        self.range = range

    # verschil tussen height en prominence
    def height_difference(self) -> int:
        return abs(self.prominence - self.height)
    
    # elke expeditie op deze berg 
    def get_expeditions(self) -> list:
        return SQL_helper.execute_query('''SELECT id, name, mountain_id, start_location, 
        date, country, duration, success FROM expeditions WHERE mountain_id = ?''', self.id)

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))