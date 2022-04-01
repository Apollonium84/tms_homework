from datetime import datetime
from exceptions import ValidationError


class Data:
    """Класс данных пользователя"""
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age

    def _clear_whitespaces(self) -> None:
        """Функция, очищающая данные от пробелов в начале и в конце"""
        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    """Класс данных пользователя, сохраняющий время создания объекта класса"""
    def __init__(self, name: str, age: str):
        super().__init__(name, age)
        self.current_time = datetime.utcnow().isoformat()


class Validator:
    """Класс валидации данных"""
    def __init__(self):
        self.data_history: list[Data] = []

    def validate(self, data: Data):
        """Функция валидации данных"""
        self.data_history.append(data)
        if self.data_history is None:
            raise ValueError

        self._validate_name()
        self._validate_age()

    def _validate_name(self) -> None:
        """ Валидация ввода имени"""
        # Проверяем имя на пустоту
        # Проверяем, что имя введено и минимальное количество символов в имени — 3
        # Проверяем количество пробелов подряд в имени

        if not self.data_history[-1].name:
            raise ValidationError("Имя не может быть пустым. ")

        if len(self.data_history[-1].name) < 3:
            raise ValidationError("Имя должно содержать хотя бы 3 символа.")

        if self.data_history[-1].name.count(" ") > 1:
            raise ValidationError("В имени не может быть двух и более пробелов подряд. ")

    def _validate_age(self) -> None:
        """ Валидация ввода возраста"""
        # Проверяем минимальный возраст 14
        # Проверяем, что возраст - не отрицательное число или 0
        if int(self.data_history[-1].age) <= 0:
            raise ValidationError("Возраст должен быть положительным числом. ")

        if int(self.data_history[-1].age) < 14:
            raise ValidationError("Минимальный возраст: 14 лет. ")
