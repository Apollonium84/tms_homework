import random
from validator import Validator, DataWithDate
from exceptions import ValidationError


def get_passport_advice(age: int) -> str | None:
    """ Даём совет по получению или замене паспорта"""

    if 16 <= age <= 17:
        return " Не забудь получить первый паспорт по достижении 16 лет. "

    if 25 <= age <= 26:
        return " Не забудь заменить паспорт по достижении 25 лет. "

    if 45 <= age <= 46:
        return " Не забудь заменить паспорт по достижении 45 лет. "

    return None


def guess_number_game(guess_start: int, guess_stop: int) -> None:
    """ Пользователь угадывает случайное число, пока не угадает """

    random_number = random.randint(guess_start, guess_stop)
    counter = 0

    while True:

        user_guess = int(input(f"Введите число от {guess_start} до {guess_stop}: "))

        if user_guess == random_number:
            print(f"Вы угадали. Вам понадобилось {counter + 1} попыток")
            break

        print("Вы не угадали")
        counter += 1

    return None


def main():
    """ Запрашиваем пользователя имя и возраст и проверяем их на нужные нам условия.
        Если условия выполнены - выводим приветствие с советом о получении паспорта,
        иначе выводим текст с ошибкой.
    """
    # Создаём объект класса Validator
    validator = Validator()
    counter = 0

    while True:
        if counter != 0:
            print(f"Попытка {counter+1}")

        name = input("Введите ваше имя: ")
        age = input("Введите ваш возраст: ")

        # Создаём объект класса DataWithDate
        data = DataWithDate(name, age)

        if counter == 0:
            start_time = data.current_time

        finish_time = data.current_time


        # Проверяем имя и возраст на подходящие условия
        try:
            validator.validate(data)
        except ValidationError as e:
            print(f"Я поймал ошибку: {e}")
            counter += 1
            continue

        # Если пользователь угадал число, то приветствуем его
        text = f"Привет, {data.name.title()}! Тебе {data.age} лет."

        # Даём совет по получению или замене паспорта
        advice = get_passport_advice(int(data.age))
        if advice:
            text += advice

        print(text)
        break
    print(f"Вам понадобилось {counter + 1} попыток "
          f"\nВремя начала: {start_time.hour}:{start_time.minute}:{start_time.second}"
          f"\nВремя окончания: {finish_time.hour}:{finish_time.minute}:{finish_time.second}"
          f"\nПродолжительность сеанса: {finish_time - start_time}\n")
    # Заставляем пользователя угадывать случайное число
    guess_number_game(1, 5)

    print("Еблан?")

