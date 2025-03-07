import sqlite3
from functions.logging import Logger


Logs = Logger()


class ConnectionMethods:
    DB_PATH = 'database/db.sqlite3'

    def connect_to_db(self):
        """Метод для подключения к базе данных"""
        self.conn = sqlite3.connect(database=self.DB_PATH)
        self.cursor = self.conn.cursor()
        Logs.info(message="Подключение установлено")

    def close_connection(self):
        """Метод для закрытия соединения с базой данных"""
        if self.conn:
            self.conn.close()
            Logs.info(message="Соединение закрыто")
