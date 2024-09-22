class PasswordManager:
    def __init__(self, *passwords):
        if len(passwords) == 0:
            raise ValueError("At least one password must be provided.")
        self.old_passwords = list(passwords)

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return "Password changed successfully."
        else:
            return "New password must be different from all past passwords."

    def is_correct(self, password):
        return password == self.get_password()

# Test usage:
manager = PasswordManager("password1", "password2", "password3")
print(manager.get_password())
print(manager.set_password("password4"))
print(manager.set_password("password2"))
print(manager.is_correct("password4"))
print(manager.is_correct("wrongpass"))
