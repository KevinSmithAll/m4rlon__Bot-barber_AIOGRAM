import sqlite3
from .reg import RegistrateMethods
from .connect import ConnectionMethods
from .ticket import TicketMethods


class Database(ConnectionMethods, RegistrateMethods, TicketMethods):
    def __init__(self):
        self.connect_to_db()

    def __del__(self):
        self.close_connection()
