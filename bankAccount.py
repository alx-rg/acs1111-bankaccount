

class BankAccount:
   def __init__(self, full_name, account_number, balance):
      self.name = full_name
      self.account = account_number
      self.balance = balance

   def describe_account(self):
      print(f'Full Name: {self.name} Account Number: {self.account} Account Balance: ${self.balance}')

   def deposit(self, amount):
      # amount = float(input("How much money would you like to deposit? "))
      self.balance += amount
      print(f'Amount Deposited: ${amount} New account Balance is: ${self.balance}')
      return self.balance

   def withdraw(self, amount):
      # amount = float(input("How much money would you like to withdraw? "))
      if (amount > self.balance):
         self.balance -= 10 
         print(f'Insufficient funds. An overdraft fee of $10 was added to your account. Your new account balance is ${self.balance}')
      else:
         self.balance -= amount
         print(f'Amount Withdrawn: ${amount} New account Balance is: ${self.balance}')
         return self.balance

   def get_balance(self):
      print(f'Hello {self.name}, your current account balance is ${self.balance}')
      return self.balance

   def add_interest(self):
      interest = self.balance * 0.00083
      print(f'Interest has accrued on your account for the ammount of ${interest}')
      self.balance += interest
      return self.balance

   def print_receipt(self):
      print('--------------------')
      print(f"{self.name}'s Statement")
      print(f'Account No.: {self.account}')
      print(f'Balance: ${self.balance}' + '\n' + '--------------------')
   

class Bank:
   def __init__(self, full_name, create_acct, deposit, withdraw, receipt):
      self.full_name = full_name
      self.create_acct = create_acct
      self.deposit = deposit
      self.withdraw = withdraw
      self.receipt = receipt

   # def full_name(self):
   # def create_acct(self):
   # def receipt(self):
   # def withdraw(self):
   # def deposit(self):

#bank = Bank ()

alex_account = BankAccount('Alex R', '12345678', 2000.00)
alex_account.describe_account()

moose_account = BankAccount('Moose Doodle', '44448888', 500)
moose_account.print_receipt()
moose_account.withdraw(550)
moose_account.add_interest()
moose_account.print_receipt()

clooney_account = BankAccount('Jim Clooney', '32323232', 1000)
clooney_account.deposit(234)
clooney_account.print_receipt()

mitchell_account = BankAccount('Mitchell SupaFly', '03141592', 2000.00)
mitchell_account.deposit(400000)
mitchell_account.print_receipt
mitchell_account.add_interest
mitchell_account.print_receipt
mitchell_account.withdraw(150)
mitchell_account.print_receipt


bank_atm = True
while bank_atm: 
    select_function = input("\n" + f"Please choose from the following Options:"+"\n"+"--------------------"+"\n"+"'1' or 'c' to create an account"+"\n"+"'2' or 'r' to get a receipt/statement"+"\n"+"'3' or 'd' to deposit money!"+"\n"+"'4' or 'w' to withdraw the money/molah"+"\n"+"'5' or 'q' to quit"+"\n"+"--------------------"+"\n")
    if select_function == 'q' or 5:
        print("Thank you for using the Python Bank")
        bank_atm = False        
    elif select_function == 'c' or 1:
        bank.create_acct()
    elif select_function == 's' or 2:
        bank.receipt()
    elif select_function == 'd' or 3:
        bank.deposit()
    elif select_function == 'w' or 4:
        bank.withdraw()


