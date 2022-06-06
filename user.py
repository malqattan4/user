from distutils.archive_util import make_archive


class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0


    def make_withdrawal(self, amount):
        self.make_withdrawal-=amount


    def display_user_balance(self):
        print(f"User: {self.name} , Balance: {self.account_balance}")


    def make_deposite(self,amount):
        self.account_balance+=amount



Maryam=user("Maryam", "m@gmail.com")
Abeer =user("Abeer", "abeer@yahoo.com")
Hettaf=user("Hettf", "halqattan@live.com")

Maryam.make_deposite(2000)
Maryam.make_deposite(300)
Maryam.make_deposite(450)
Maryam.make_withdrawal(260)
Maryam.display_user_balance()

Abeer.make_deposite(4500)
Abeer.make_deposite(200)
Abeer.make_withdrawal(50)
Abeer.make_withdrawal(200)
Abeer.display_user_balance()

Hettaf.make_deposite(3700)
Hettaf.make_withdrawal(450)
Hettaf.make_withdrawal(100)
Hettaf.make_withdrawal(200)
Hettaf.display_user_balance()
