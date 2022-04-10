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


def main():
    """ Проверяем существование логина у пользователя:
     если есть - авторизовываем,
     иначе регисртируем
    """
    user = Authenticator()
    if user.login is None:
        print("Вы проходите регистрацию")
    else:
        print("Вы авторизовываетесь")

    while True:

        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if user.login is None:
            try:
                user.registrate(login, password)
            except RegistrationError as e:
                print(f"{e}")
                continue
            print("Вы зарегистрировались")

        try:
            user.authorize(login, password)
        except AuthorisationError as e:
            print(f"{e}")
            continue

        break

    # Заставляем пользователя угадывать случайное число
    guess_number_game(1, 5)


main()
