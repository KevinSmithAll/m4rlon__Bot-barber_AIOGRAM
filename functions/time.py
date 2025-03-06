import re


def is_valid_time(time_string: str) -> bool:
    # Регулярное выражение для проверки формата ЧЧ.ММ
    time_pattern = r'^([01]\d|2[0-3])\.[0-5]\d$'
    # Проверяем соответствие строки шаблону
    return True if re.match(time_pattern, time_string) else False
