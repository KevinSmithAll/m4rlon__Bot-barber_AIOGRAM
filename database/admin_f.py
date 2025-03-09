import sqlite3
from datetime import datetime
import functions.date as date_func


class AdminsMethods():

    CHECK_TODAY_QUERY = """SELECT name, phone, date, time FROM tickets WHERE date=(?)"""

    def check_today(self):
        date = date_func.get_date_today()
        self.cursor.execute(self.CHECK_TODAY_QUERY, (date,))
        return self.cursor.fetchall()

    def check_tickets_7_days(self) -> list:
        all_tickets = {}
        dates = date_func.get_seven_dates()
        for date in dates:
            self.cursor.execute(self.CHECK_TODAY_QUERY, (date,))
            all_tickets[date] = self.cursor.fetchall()
        return all_tickets
