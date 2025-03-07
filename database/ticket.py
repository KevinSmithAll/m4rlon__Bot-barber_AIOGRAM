import sqlite3
from functions.logging import Logger


Logs = Logger()


class TicketMethods():

    TICKET_QUERY = """INSERT INTO tickets (user_id, name, phone, date, time) SELECT u.user_id, (?), (?), (?), (?) FROM users u WHERE u.tg_id = (?)"""
    CHECK_TICKET_QUERY = """SELECT t.time FROM tickets t WHERE t.date = (?)"""
    CHECK_MY_TICKET_QUERY = """SELECT t.date, t.time FROM tickets t WHERE t.user_id = (SELECT u.user_id FROM users u WHERE u.tg_id = (?))"""

    def create_ticket(self,
                      tg_id: int,
                      name: str,
                      phone: str,
                      date: str,
                      time: str):
        try:
            self.cursor.execute(self.TICKET_QUERY,
                                (name, phone, date, time, tg_id))
            self.conn.commit()
            Logs.info(
                message=f'Пользователь {name} записался на {date}, {time}. Его телефон {phone}')
        except sqlite3.Error as e:
            Logs.error(message=e)

    def check_ticket(self, date: str) -> list[str]:
        self.cursor.execute(self.CHECK_TICKET_QUERY, (date,))
        all_tickets = self.cursor.fetchall()
        not_available_times = []
        for ticket in all_tickets:
            not_available_times.append(ticket[0])
        return not_available_times

    def check_my_ticket(self, tg_id: int):
        self.cursor.execute(self.CHECK_MY_TICKET_QUERY, (tg_id,))
        return self.cursor.fetchall()
