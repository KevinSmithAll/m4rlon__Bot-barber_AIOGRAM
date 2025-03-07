import logging


class Logger:
    def __init__(self, log_file_path='logs.log'):
        # Имя логгера можно задать произвольно
        self.logger = logging.getLogger(__name__)
        # Устанавливаем минимальный уровень логирования
        self.logger.setLevel(logging.DEBUG)

        # Создаем обработчики для записи в файл и на консоль
        file_handler = logging.FileHandler(
            log_file_path,
            encoding='utf-8',
            mode='w')

        # Форматтер для сообщений
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        # Присваиваем форматтер обоим обработчикам
        file_handler.setFormatter(formatter)

        # Добавляем обработчики к логгеру
        self.logger.addHandler(file_handler)

    def debug(self, message):
        """Запись отладочного сообщения"""
        self.logger.debug(message)

    def info(self, message):
        """Запись информационного сообщения"""
        self.logger.info(message)

    def warning(self, message):
        """Запись предупреждающего сообщения"""
        self.logger.warning(message)

    def error(self, message):
        """Запись сообщения об ошибке"""
        self.logger.error(message)

    def critical(self, message):
        """Запись критического сообщения"""
        self.logger.critical(message)
