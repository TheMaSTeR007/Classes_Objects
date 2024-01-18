class BankAccount:
    def __init__(self, name, balance=0): # Using __init__ method we dont have to explicitely set details of each instance of this class, as python will call set details implicitely instead of creating manually expilcitely. We should pass values while creating instances of the class!
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Account Holder Name : {self.name}")
        print(f"Account Balance : {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited to Account of {self.name}")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} is withdrawn to Account of {self.name}")

# Creating instances of the BankAccount class
Person_1 = BankAccount('Jaimin',10) # here we pass values while creating instance of class together
Person_2 = BankAccount('raj',5) # here we pass values while creating instance of class together

# Hence,we don't need to call it here manually.
# Calling set_details method on each instance
# Person_1.set_details('Jaimin',10)
# Person_2.set_details('raj',5)

# Calling display method on each instance
Person_1.display()
Person_2.display()

# Calling deposit method on Person_1 & displaying balance after transactions
Person_1.deposit(10)
Person_1.display()

# Calling deposit method on Person_2 & displaying balance after transactions
Person_2.deposit(5)
Person_2.display()

# Calling withdraw method on Person_1 & displaying balance after transactions
Person_1.withdraw(3)
Person_1.display()

# Calling withdraw method on Person_2 & displaying balance after transactions
Person_2.withdraw(2)
Person_2.display()
