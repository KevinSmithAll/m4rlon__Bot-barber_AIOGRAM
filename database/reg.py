import sqlite3
from functions.logging import Logger


Logs = Logger()


class RegistrateMethods:
    REG_QUERY = """INSERT INTO users (tg_id) VALUES (?)"""

    def new_user(self, tg_id):
        try:
            self.cursor.execute(self.REG_QUERY, (tg_id,))
            self.conn.commit()
            Logs.info(
                message=f"Пользователь '{tg_id}'успешно добавлен в БД пользователей")
            return True
        except sqlite3.IntegrityError:
            return False
