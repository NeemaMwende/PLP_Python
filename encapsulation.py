# class Car:
#     def __init__(self, make, model):
#         self.__make = make
#         self.__model = model

#     def get_make(self):
#         return self.__make

#     def get_model(self):
#         return self.__model

# my_car = Car("Toyota", "Corolla")
# print(my_car.get_make())  # Output: Toyota
# print(my_car.get_model())  # Output: Corolla

#another example
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """Method to deposit money into the account"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance is ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Method to withdraw money from the account"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.__balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        """Method to get the current balance"""
        return self.__balance

# Create a bank account object
account = BankAccount("123456789", 1000)

# Deposit money
account.deposit(500)  # Output: Deposited $500. New balance is $1500.

# Withdraw money
account.withdraw(200)  # Output: Withdrew $200. New balance is $1300.

# Check balance
print("Current balance:", account.get_balance())  # Output: Current balance: 1300

# Attempt to access private attributes directly (will raise an AttributeError)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError
