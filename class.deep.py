''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHEITENCE
    (3) POLYMORPHISM
'''

print("===== ENCAPSULATION =====")
# ENCAPSULATION > punlic __private _protected

class Account():
    # state
    description = "The class makes bank accoints"
    
    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount
        
        
    # method 
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")
        
        
    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount
        
        
    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount
         
         
    @property
    def holder(self):
        return self.__owner

    
    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner
        
    
    

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Ellianor", 5000)
my_account.get_balance()


print("_______________")
my_account.deposit(4800)
my_account.withdraw(100)
my_account.get_balance()


print("_______________")

# state 
# getter and setter
print("owner before:", my_account.holder)


my_account.holder = "Mery"
print("owner after:", my_account.holder)