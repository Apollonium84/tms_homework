from datetime import datetime
from os.path import exists


class AuthorisationError(Exception):
    """Класс ошибок авторизации"""
    pass


class RegistrationError(Exception):
    """Класс ошибок регистроации"""
    pass


class Authenticator:
    """Класс аутентификации"""
    def __init__(self):

        self.login: str | None = None
        self.password: str | None = None
        self.last_success_login_at: str | None = ""
        self.errors_count: int = 0

        if self._is_auth_file_exists():
            self._read_auth_file()

    def _is_auth_file_exists(self) -> bool:
        """Проверка существования файла в директории"""
        file_exists = exists("auth.txt")
        return file_exists

    def _read_auth_file(self):
        """Прочтение файла """

        with open("auth.txt") as f:
            self.login = f.readline().strip()
            self.password = f.readline().strip()
            self.last_success_login_at = f.readline()
            self.errors_count = int(f.readline().strip())

    def authorize(self, login, password):
        """Авторизация пользователя"""
        if self.login is None:
            raise AuthorisationError("Отсутствует логин")

        if self.login != login or self.password != password:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorisationError("Неверный логин или пароль")

        self.last_success_login_at = datetime.utcnow().isoformat()

        self._update_auth_file()

    def _update_auth_file(self):
        """Обновление файла"""
        with open("auth.txt", "w") as f:
            f.write(f"{self.login}\n")
            f.write(f"{self.password}\n")
            f.write(f"{self.last_success_login_at}\n")
            f.write(str(f"{self.errors_count}"))

    def registrate(self, login: str, password: str):
        """Регистрация пользователя"""
        if self._is_auth_file_exists():
            raise RegistrationError("Файл уже существует")
        if self.login:
            raise RegistrationError("Логин уже существует")
        self.login = login
        self.password = password

        self._update_auth_file()

