import re
from datetime import datetime


def is_valid_date(date_string: str) -> bool:
    # Регулярное выражение для проверки формата ДД.ММ.ГГГГ
    date_pattern = r'^\d{2}\.\d{2}\.\d{4}$'
    # Проверяем соответствие строки шаблону
    return True if re.match(date_pattern, date_string) else False


def is_past(date_string: str) -> bool:
    if is_valid_date(date_string):
        try:
            # Преобразуем строку в объект datetime
            input_date = datetime.strptime(date_string, '%d.%m.%Y')
            # Получаем текущую дату
            current_date = datetime.now()
            # Сравниваем даты
            if input_date.date() < current_date.date():
                return False
            else:
                return True

        except ValueError as e:
            return False
    else:
        return False
