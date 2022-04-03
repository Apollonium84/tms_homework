from datetime import datetime
from os.path import exists


class AuthorisationError(Exception):
    pass


class RegistrationError(Exception):
    pass


class Authenticator:
    def __init__(self):

        self.login: str | None = None
        self.password: str | None = None
        self.last_success_login_at: str | None = None
        self.errors_count: int = 0

        if self._is_auth_file_exists():
            self._read_auth_file()

    def _is_auth_file_exists(self) -> bool:
        file_exists = exists("homework_9/auth.txt")
        return file_exists

    def _read_auth_file(self):

        with open("homework_9/auth.txt") as f:
            self.login = f.readline().strip()
            self.password = f.readline().strip()
            self.last_success_login_at = f.readline()
            self.errors_count = int(f.readline().strip())

    def authorize(self, login, password):
        if self.login != login or self.password != password:
            self.errors_count += 1
            raise AuthorisationError("gg")

        self.last_success_login_at = datetime.utcnow().isoformat()

        self._update_auth_file()

    def _update_auth_file(self):
        with open("homework_9/auth.txt", "w") as f:
            f.write(self.login)
            f.write(self.password)
            f.write(self.last_success_login_at)
            f.write(str(self.errors_count))

    def registrate(self, login: str, password: str):
        if self._is_auth_file_exists():
            raise RegistrationError("Файл уже существует")
        if self.login:
            raise RegistrationError("Логин уже существует")
        self.login = login
        self.password = password
        with open("homework_9/auth.txt", "w") as f:
            f.write(self.login)
            f.write(self.password)
            f.write(self.last_success_login_at)
            f.write(str(self.errors_count))
