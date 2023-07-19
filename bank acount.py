class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self, amount):
        self.balance += amount
        return amount
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount
    def check_balance(self):
        print(f"The current balance is {self.balance}")
    def customer_details(self):
        print(f"Customer name: {self.customer_name}")
        print(f"Account number: {self.account_number}")
        print(f"Date of account opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")