import random
from authenticator import Authenticator, RegistrationError, AuthorisationError


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


def while_true(func):
    def wrapper():
        while True:
            result = func()
            if result is True:
                break

    return wrapper


authenticator = Authenticator()


@while_true
def main() -> bool:
    """ Проверяем существование логина у пользователя:
     если есть - авторизовываем,
     иначе регисртируем
    """

    if authenticator.login is None:
        print("Вы проходите регистрацию")

        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        try:
            authenticator.registrate(login, password)
        except RegistrationError as e:
            print(f"{e}")
            return False

        print("Вы зарегистрировались")
        return False

    else:
        print("Вы авторизовываетесь")

        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        try:
            authenticator.authorize(login, password)
        except AuthorisationError as e:
            print(f"{e}")
            return False

        print("Вы авторизовались")

    # Заставляем пользователя угадывать случайное число
    guess_number_game(1, 5)
  
    return True


main()
