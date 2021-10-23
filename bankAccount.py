class BankAccount:
   def __init__(self, full_name, account_number, balance):
      self.name = full_name
      self.account = account_number
      self.balance = balance

   def describe_account(self):
      print(f'Full Name: {self.name} Account Number: {self.account} Account Balance: ${self.balance}')

   def deposit(self):
      deposit_amount = float(input("How much money would you like to deposit? "))
      self.balance += deposit_amount
      print(f'Amount Deposited: ${deposit_amount}')
      print(f'New account Balance is: ${self.balance}')
      return self.balance

   def withdraw(self):
      withdraw_amount = float(input("How much money would you like to withdraw? "))
      self.balance -= withdraw_amount
      print(f'Amount Withdrawn: ${withdraw_amount}')
      print(f'New account Balance is: ${self.balance}')
      return self.balance

   def get_balance(self):

   def add_interest(self):

   


alex_account = BankAccount('Alex R', 12345678, 2000.80)
alex_account_statement = alex_account.describe_account()

moose_account = BankAccount('Moose Doodle', 44448888, 1000)
moose_account_withdraw = moose_account.withdraw()

clooney_account = BankAccount('Moose Doodle', 44448888, 1000)
clooney_account_deposit = clooney_account.deposit()
