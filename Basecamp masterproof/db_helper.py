import sys
import os
import sqlite3 as sql

class SQL_helper:
    
    def __init__(self, db_name) -> None:
        db_conn = sql.connect(os.path.join(sys.path[0], db_name + ".db"))
        self.sql_conn = db_conn

    def execute_query(self, query:str, values:any=[], fetch:str='') -> None or list:
        match fetch:
            case 'one':
                data = self.sql_conn.execute(query, values).fetchone()
                if data == None:
                    return 'not_found'
                return data[0]
            case 'all':
                return self.sql_conn.execute(query, values).fetchall()
            case other:
                try:
                    self.sql_conn.execute(query, values)
                except sql.Warning:
                    self.sql_conn.executescript(query)
                self.sql_conn.commit()