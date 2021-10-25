#Import random to randomize the account number
from random import randint

# Create a BankAccount class to store the data for each account
class BankAccount:
   def __init__(self, full_name, account_type, account_number, balance):
      self.name = full_name
      self.account_type = account_type
      self.account = account_number
      self.balance = balance

   # Deposit a certain "amount" into account and return the updated account balance
   def deposit(self, amount):
      self.balance += amount
      print(f'Amount Deposited: ${amount} New account Balance is: ${self.balance}')
      return self.balance

   # Withdraw a certain "amount" from the account and return the updated account balance
   def withdraw(self, amount):
      # IF the balance in the account is less than the amount to withdraw, debit 10$ from the account and return overdraft message.
      if (amount > self.balance):
         self.balance -= 10 
         print(f'You have insufficient funds to withdraw ${amount}. An overdraft fee of $10 was added to your account. Your new account balance is ${self.balance}')
      # If balance is greater than amount withdrawn, show new balance
      else:
         self.balance -= amount
         print(f'Amount Withdrawn: ${amount} New account Balance is: ${self.balance}')
         return self.balance

   # When the interest function is called, calculate interest and add it to the account balance.
   def add_interest(self):
      #Check to see if the account type is Checking or Saving and calculate amount of interest earned accordingly.
      if (self.account_type == 'Checking'):
         interest = self.balance * 0.00083
      else:
         interest = self.balance * 0.001
      #Print interest earned with two decimal spaces and then add the interest to the account balance.
      print(f'Interest has accrued on your {self.account_type} account for the ammount of ${"{:.2f}".format(interest)}')
      self.balance += interest
      return self.balance

   # Print all account information for user and hide the first 4 digits of account with a "*"
   def print_receipt(self):
      print('--------------------')
      print(f"{self.name}'s Statement")
      print(f'Account Type: {self.account_type}')
      print(f'Account No.: ****{str(self.account)[slice(4,8)]}')
      print(f'Balance: ${"{:.2f}".format(self.balance)}' + '\n' + '--------------------')
   

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


# Use Random to assign an 8 digit bank account number when function is called
def random_bank_account():
   random_number = randint(00000000,99999999)
   account_number = str(random_number)
   return account_number
      


# TEST functions below:

#Check to see if deposit and Savings account interest works
alex_account = BankAccount('Alex Supafly', 'Saving', random_bank_account(), 5000.00)
alex_account.print_receipt()
alex_account.deposit(5000)
alex_account.print_receipt()
alex_account.add_interest()
alex_account.print_receipt()

#Check to see if overdraft fee works
moose_account = BankAccount('Moose Doodle', 'Saving', random_bank_account(), 500)
moose_account.withdraw(550)
moose_account.print_receipt() 

#Check to see if Checking account interest works
clooney_account = BankAccount('Jim Clooney', 'Checking', random_bank_account(), 10000)
clooney_account.print_receipt()
clooney_account.add_interest()
clooney_account.print_receipt()

#Check to see if data given to us for assignment works
mitchell_account = BankAccount('Mitchell', 'Checking', '03141592' , 2000.00)
mitchell_account.print_receipt()
mitchell_account.deposit(400000)
mitchell_account.print_receipt()
mitchell_account.add_interest()
mitchell_account.print_receipt()
mitchell_account.withdraw(150) 
mitchell_account.print_receipt() 

