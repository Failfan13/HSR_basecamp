from datetime import datetime
from db_helper import SQL_helper

class Climber:

    def __init__(self, id:int, first_name:str, last_name:str, nationality:str, date_of_birth:datetime) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth

    # Hier moet de leeftijd gevonden worden.
    def get_age(self) -> int:
        return abs((datetime.now().year - self.date_of_birth.year))
    
    # Hier moet een list gereturned worden ? dit kan waar de klimmer op is geweest en gewoon alle expeditions
    def get_expeditions(self, sql_conn = SQL_helper('climbersapp')) -> list:
        print(sql_conn)
        # get_expedition_id = SQL_helper.execute_query('''SELECT expedition_id 
        #     FROM expedition_climbers WHERE climber_id = ?''', self.id, fetch='all')
        # get_expedition_name = SQL_helper.execute_query('''SELECT id, name, mountain_id, 
        #     start_location, data, country, duration, success
        #         FROM expeditions WHERE id = ?''', get_expedition_id)
        # return get_expedition_id

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))