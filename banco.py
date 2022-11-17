
class Bank:
    balance = 0
    daily_witdraw = 0

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            print("Unavailable balance")
        else:
            if not self.daily_witdraw > 3:
                print("Withdraw successfully")
                self.balance -= value
                self.daily_witdraw += 1
            else:
                print("Maximum withdraw permited")

    def extract(self):
        print(f"Balance: R$ {self.balance:.2f}")

bank = Bank()

option = -1

while option != 4:
    option = int(input("[1]: Deposit\n[2]: Withdraw\n[3]: Extract\n[4]: Exit\n"))
    if option == 1:
        value = int(input("What value would you like to deposit? "))
        bank.deposit(value)
    elif option == 2:
        value = int(input("What value would you like to withdraw? "))
        bank.withdraw(value)
    elif option == 3:
        print("Your Balance".center(20, "#"))
        bank.extract()
        print("".center(20, "#"))
    else:
        print("Thanks you, and see you later!")
        exit()
    