import json
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
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0

        if self._is_auth_file_exists():
            self._read_auth_file()

    @staticmethod
    def _is_auth_file_exists() -> bool:
        """Проверка существования файла в директории"""
        file_exists = exists("auth.json")
        return file_exists

    def _read_auth_file(self):
        """Прочтение файла """

        with open("auth.json") as f:
            file_data = f.readline()
        print(type(json.loads(file_data)))
        data = json.loads(file_data)
        self.login = data["login"]
        self.password = data["password"]
        self.last_success_login_at = data["last success login at"].fromisoformat()
        self.errors_count = data["errors count"]

    def authorize(self, login, password):
        """Авторизация пользователя"""
        if self.login is None:
            raise AuthorisationError("Отсутствует логин")

        if self.login != login or self.password != password:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorisationError("Неверный логин или пароль")

        self.last_success_login_at = datetime.utcnow()

        self._update_auth_file()

    def _update_auth_file(self):
        """Обновление файла"""

        data = {"login": self.login, "password": self.password,
                "last success login at": self.last_success_login_at.isoformat(), "errors count": self.errors_count}
        parsed_data = json.dumps(data)
        with open("auth.json", "w") as f:
            f.write(parsed_data)

    def registrate(self, login: str, password: str):
        """Регистрация пользователя"""
        if self._is_auth_file_exists():
            raise RegistrationError("Файл уже существует")
        if self.login:
            raise RegistrationError("Логин уже существует")

        self.login = login
        self.password = password
        self.last_success_login_at = datetime.utcnow()

        self._update_auth_file()
