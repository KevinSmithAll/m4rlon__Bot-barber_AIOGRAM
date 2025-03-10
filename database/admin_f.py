import sqlite3
from datetime import datetime
import functions.date as date_func
import pandas as pd
from io import BytesIO


class AdminsMethods():

    CHECK_TODAY_QUERY = """SELECT name, phone, date, time FROM tickets WHERE date=(?) AND ready=0"""
    READY_QUERY = """INSERT INTO ready_tickets (ticket_id) SELECT ticket_id FROM tickets WHERE date=(?) AND time=(?)"""
    IS_TICKET = """SELECT ticket_id FROM tickets WHERE date=(?) AND time=(?)"""
    NOT_READY_QUERY = """INSERT INTO not_ready_tickets (ticket_id, comment) SELECT ticket_id, (?) FROM tickets WHERE date=(?) AND time=(?)"""
    UPDATE_TICKET_QUERY = """UPDATE tickets SET ready=1 WHERE date=(?) AND time=(?)"""
    CALC_READY = """SELECT COUNT(*) FROM ready_tickets"""
    CALC_NOT_READY = """SELECT COUNT(*) FROM not_ready_tickets"""

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
        df = df.rename(
            columns={"name": "Фамилия", "phone": "Телефон", "date": "Дата", "time": "Время"})
        # Буферизация данных в памяти
        # Создание объекта BytesIO для временного хранения данных
        buffer = BytesIO()
        # Сохранение данных в Excel-файл в память
        writer = pd.ExcelWriter(buffer, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Records', index=True)
        writer.close()
        buffer.seek(0)
        return buffer

    def mark_ready(self, date: str, time: str) -> None:
        self.cursor.execute(self.IS_TICKET, (date, time))
        if self.cursor.fetchone():
            self.cursor.execute(self.UPDATE_TICKET_QUERY, (date, time))
            self.cursor.execute(self.READY_QUERY, (date, time))
            self.conn.commit()
        else:
            raise ValueError("Ticket not found")

    def mark_not_ready(self, date: str, time: str, comment: str) -> None:
        self.cursor.execute(self.IS_TICKET, (date, time))
        if self.cursor.fetchone():
            self.cursor.execute(self.NOT_READY_QUERY, (comment, date, time))
            self.conn.commit()
        else:
            raise ValueError("Ticket not found")

    def get_ready_tickets(self) -> int:
        self.cursor.execute(self.CALC_READY)
        return self.cursor.fetchone()[0]

    def get_not_ready_tickets(self) -> int:
        self.cursor.execute(self.CALC_NOT_READY)
        return self.cursor.fetchone()[0]
