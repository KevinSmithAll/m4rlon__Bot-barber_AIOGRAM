import sqlite3
from .reg import RegistrateMethods
from .connect import ConnectionMethods
from .ticket import TicketMethods
from .admin_f import AdminsMethods


class Database(ConnectionMethods, RegistrateMethods, TicketMethods, AdminsMethods):
    def __init__(self):
        self.connect_to_db()

    def __del__(self):
        self.close_connection()
