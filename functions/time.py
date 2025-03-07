from datetime import datetime


def get_dayweek(date: str) -> str:
    # Разбиваем строку даты на части
    day, month, year = map(int, date.split('.'))

    # Создаем объект datetime
    date_obj = datetime(year, month, day)

    # Получаем название дня недели
    return date_obj.strftime('%A')


def get_avaliable_time(date: str) -> tuple:
    dayweeks = ('Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday')
    weekends = ('Saturday', 'Sunday')

    dayweek_times = ('19.00', '20.00', '21.00', '22.00')
    saturday_times = ('16.00', '17.00', '18.00', '19.00',
                      '20.00', '21.00', '22.00', '23.00')
    sunday_times = ('08.00', '09.00', '10.00', '11.00', '12.00')

    day = get_dayweek(date)

    if day in dayweeks:
        return dayweek_times
    elif day in weekends:
        if day == 'Saturday':
            return saturday_times
        else:
            return sunday_times
