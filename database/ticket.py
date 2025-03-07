import sqlite3


class TicketMethods():

    TICKET_QUERY = """INSERT INTO tickets (user_id, name, phone, date, time) SELECT u.user_id, (?), (?), (?), (?) FROM users u WHERE u.tg_id = (?)"""
    CHECK_TICKET_QUERY = """SELECT t.time FROM tickets t WHERE t.date = (?)"""

    def create_ticket(self,
                      tg_id,
                      name,
                      phone,
                      date,
                      time):
        try:
            self.cursor.execute(self.TICKET_QUERY,
                                (name, phone, date, time, tg_id))
            self.conn.commit()
            print('Ticket created')
        except sqlite3.Error as e:
            print(e)

    def check_ticket(self, date):
        self.cursor.execute(self.CHECK_TICKET_QUERY, (date,))
        return self.cursor.fetchall()
