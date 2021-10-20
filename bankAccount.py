class BankAccount:
   def __init__(self, full_name, account_number, balance):
      self.name = full_name
      self.account = account_number
      self.balance = balance
   def describe_account(self):
      print(f'Full Name: {self.name} Account Number: {self.account} Account Balance: ${self.balance}')
      #return f'Name: {self.name} type: {self.type} Has Milk: {self.milk}'

alex_account = BankAccount('Alex r', 12345678, 100500999)
alex_account_statement = alex_account.describe_account()
