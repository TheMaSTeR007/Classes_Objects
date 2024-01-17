class BankAccount:
    def set_details(self, name, balance=0):
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
Person_1 = BankAccount()
Person_2 = BankAccount()

# Calling set_details method on each instance
Person_1.set_details('Jaimin',10)
Person_2.set_details('raj',5)

# Calling display method on each instance
Person_1.display()
Person_2.display()

# Calling deposit method on Person_1 & displaying balance after transactions
Person_1.deposit(10)
Person_1.display()

# Calling deposit method on Person_1 & displaying balance after transactions
Person_2.deposit(5)
Person_2.display()

# Calling withdraw method on Person_1 & displaying balance after transactions
Person_1.withdraw(3)
Person_1.display()

# Calling withdraw method on Person_1 & displaying balance after transactions
Person_2.withdraw(2)
Person_2.display()
