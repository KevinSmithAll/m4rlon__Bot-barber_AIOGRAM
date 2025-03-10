import sqlite3
from datetime import datetime
import functions.date as date_func
import pandas as pd
from io import BytesIO


class AdminsMethods():

    CHECK_TODAY_QUERY = """SELECT name, phone, date, time FROM tickets WHERE date=(?)"""
    INSERT_BLOB_QUERY = """INSERT INTO users_exports (tg_id, export_xlsx) VALUES (?, ?)"""

    def check_today(self) -> list[tuple]:
        date = date_func.get_date_today()
        self.cursor.execute(self.CHECK_TODAY_QUERY, (date,))
        return self.cursor.fetchall()

    def check_tickets_7_days(self) -> dict:
        all_tickets = {}
        dates = date_func.get_seven_dates()
        for date in dates:
            self.cursor.execute(self.CHECK_TODAY_QUERY, (date,))
            all_tickets[date] = self.cursor.fetchall()
        return all_tickets

    def check_any_day(self, date: str) -> list[tuple]:
        self.cursor.execute(self.CHECK_TODAY_QUERY, (date,))
        return self.cursor.fetchall()

    def get_bytes(self):
        df = pd.read_sql_query(
            "SELECT name, phone, date, time FROM tickets", self.conn)

        # Буферизация данных в памяти
        # Создание объекта BytesIO для временного хранения данных
        buffer = BytesIO()
        # Сохранение данных в Excel-файл в память
        writer = pd.ExcelWriter(buffer, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Records', index=False)
        writer.close()

        # Установка позиции в буфере на начало
        buffer.seek(0)

        return buffer
