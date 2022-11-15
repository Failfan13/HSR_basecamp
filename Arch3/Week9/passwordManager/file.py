class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self) -> str:
        return self.old_passwords[-1]

    def set_password(self, password: any) -> None:
        if (password not in self.old_passwords):
            self.old_passwords.append(password)

    def is_correct(self, str: str) -> bool:
        return str == self.old_passwords[-1]
