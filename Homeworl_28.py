class BankUser:
    MAX_PASSWORD_ENTRY =3

    def __init__(self, first_name, last_name, age, account_number, balance, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_number = account_number
        self.balance = balance
        self.password = password
        self.password_entry = 0

    def is_valid_input(self):
        if isinstance(self.first_name, str) and isinstance(self.last_name, str) and isinstance(self.age,
                    int) and isinstance(self.account_number,str) and isinstance(self.balance, float) and isinstance(self.password, str):
            if len(self.account_number) == 16 and len(self.password) >= 8:
                return True
        return False

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        return self.age

    def get_account_info(self, password_catch):
        if password_catch == self.password:
            return self.account_number, self.balance
        else:
            self.password_entry+=1
            if self.password_entry>=self.MAX_PASSWORD_ENTRY:
                return " You entered the password wrong 3 times , account locked"
            else:
                return "Incorrect password"

    def deposit_plus(self, password_catch, chash):
        if password_catch == self.password:
            if chash > 0:
                self.balance += chash
                return f"{self.balance}$"
            else:
                return "chash must be positive"
        else:
            self.password_entry += 1
            if self.password_entry >= self.MAX_PASSWORD_ENTRY:
                return " You entered the password wrong 3 times , account locked"
            else:
                return "Incorrect password"

    def deposit_minus(self, password_catch, chash):
        if password_catch == self.password:
            if chash > 0 and chash <= self.balance:
                self.balance -= chash
                return f"{self.balance}$"
            else:
                return "Invalid chash or balance"
        else:
            self.password_entry += 1
            if self.password_entry >= self.MAX_PASSWORD_ENTRY:
                return "You entered the password wrong 3 times , account locked"
            else:
                return "Incorrect password "


user = BankUser("Armen", "Shekikyan", 28, "1234567890123456", 1000.0, "password121")
print(user.is_valid_input())  # True
print(user.get_age())   # Armen Shekikyan
print(user.get_full_name()) # 28
print(user.get_account_info("password111")) #1234567890123456 , 1000
print(user.deposit_plus("password111", 500)) 
print(user.deposit_minus("password111", 200))
