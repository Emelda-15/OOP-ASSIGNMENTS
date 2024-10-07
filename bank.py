class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    # Method to deposit an amount.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("The deposit amount should be positive.")

    # Method to withdraw an amount.
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    # Class variable (interest rate)
    interest_rate = 0.05

    # Method to apply interest based on class variable interest_rate
    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    # Method to display account information.
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance:.2f}")


# Creating two instances of BankAccount with different account holders
account1 = BankAccount("Sheba")
account2 = BankAccount("Gavin")

# Performing deposits and withdrawals
account1.deposit(10000)
account1.withdraw(5000)
account1.apply_interest()

account2.deposit(1000)
account2.withdraw(500)
account2.apply_interest()

# Displaying account information
account1.display_account_info()
account2.display_account_info()
