import sqlite3


class RegistrateMethods:
    REG_QUERY = """INSERT INTO users (tg_id) VALUES (?)"""

    def new_user(self, tg_id):
        try:
            self.cursor.execute(self.REG_QUERY, (tg_id,))
            self.conn.commit()
            print(f"Пользователь '{tg_id}'успешно добавлен")
            return True
        except sqlite3.IntegrityError:
            print(f"Пользователь '{tg_id}' уже существует")
            return False
