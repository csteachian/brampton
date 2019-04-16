# NC Tutorial 18 - OOPS example

class account:
    # PRIVATE account_no : STRING
    # PRIVATE balance : REAL
    # PRIVATE customer : STRING
    
    def __init__(self):
        self.__accountno = "0000000000"
        self.__balance = 0.0
        self.__customer = ""

    def set_accountno(self,this_accountno):
        self.__accountno = this_accountno

    def set_balance(self,this_balance):
        self.__balance = this_balance

    def set_customer(self,this_customer):
        self.__customer = this_customer

    def get_accountno(self):
        return self.__accountno

    def get_customer(self):
        return self.__customer

    def get_balance(self):
        return self.__balance
    
    def display_details(self):
        print("========================================")
        print("Customer name:",self.get_customer())
        print("Account no:",self.get_accountno())
        print("Balance: £{:.2f}".format(self.get_balance()))

class savings_account(account): # inheritance
    # PRIVATE interest : REAL

    def __init__(self,accountno,customer,balance):
        account.__init__(self) # inheritance
        account.set_accountno(self,accountno) # inheritance
        account.set_customer(self,customer) # inheritance
        account.set_balance(self,balance) # inheritance
        self.__interest = 3.0

    def display_details(self): # polymorphism
        print("========================================")
        print("Customer name:",self.get_customer())
        print("Account no:",self.get_accountno())
        print("Balance: £{:.2f}".format(self.get_balance()))
        print("Interest rate: {:.1f}%".format(self.__interest))
        

new_bank = account()
new_bank.set_accountno("1234567890")
new_bank.set_customer("Mr Ian Simpson")
new_bank.set_balance(700.0)
new_bank.display_details()

new_bank2 = savings_account("1234567891","Ms Nicole Carrera",1000.0)
new_bank2.display_details()
