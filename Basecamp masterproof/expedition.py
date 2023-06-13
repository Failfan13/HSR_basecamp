from datetime import datetime
from db_helper import SQL_helper

class Expedition:

    def __init__(self, id:int, name:str, mountain_id:int, start:str, date:datetime, country:str, duration:int, success:bool) -> None:
        self.id = id
        self.name = name
        self.mountain_id = mountain_id
        self.start = start
        self.date = date
        self.country = country
        self.duration = duration
        self.success = success
    # Voeg een climber toe aan database expeditie_climbers via het id van de climber en de expedieties id
    def add_climber(self, climber:object) -> None:
        SQL_helper.execute_query('''INSERT INTO expedition_climbers (climber_id, expedition_id)
                VALUES (?, ?)''', [climber.get('id'), self.id])
    # Krijgt een lijst van climmers op basis van alle climmer_id's in de expedition database met die id
    def get_climbers(self) -> list:
        climber_ids = SQL_helper.execute_query('''SELECT climber_id FROM expedition_climbers
                WHERE expedition_id = ?''', self.id, fetch='all')
        return SQL_helper.execute_query('''SELECT id, first_name, last_name, nationality, date_of_birth}
                FROM climbers WHERE id IN ?''', climber_ids)
    # Vragen van berg in database
    def get_mountain(self) -> list:
        return SQL_helper.execute_query('''SELECT id, name, country, rank, height, prominence, range
            FROM mountains WHERE id = ?''', self.mountain_id)
    # Veranderd een datum van een expeditie date(datetime) naar string
    def convert_date(self) -> str:
        return datetime.strftime(self.date, '%Y-%m-%d')
    # Veranderd een duration(minuten) naar aantal dagen uren minuten
    def convert_duration(self) -> str:
        ...

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join(
            [f"{key}={value!r}" for key, value in self.__dict__.items() if not key == 'sql_conn']))