import sqlite3


class TicketMethods():

    TICKET_QUERY = """INSERT INTO tickets (user_id, name, phone, date, time) SELECT u.user_id, (?), (?), (?), (?) FROM users u WHERE u.tg_id = (?)"""

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
