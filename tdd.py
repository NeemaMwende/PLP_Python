#Test-driven development (TDD) is a software development practice where developers write tests before writing the actual code.
# Add tests > see tests fail > write code > run tests > refactor > add tests
#testing frameworks : unittest, pytest, nose : provide test discvery, test fixtures and test reporting

# import unittest
# class Tdd_Python(unittest.TestCase):
#     def test_banking_credit_method_returns_correct_result(self):
#         bank = Banking()
#         final_bal = bank.credit(1000)
#         self.assertEqual(final_bal, 1000)


# import unittest
# def add(a, b):
#     return a + b
# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         result = add(10, 20)
#         self.assertEqual(result, 30)
# if __name__ == "__main__":
#     unittest.main()


import unittest

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance

class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount()
        print("Testing initial balance...")
        self.assertEqual(account.get_balance(), 0)
        print(f"Initial balance: {account.get_balance()}")
    
    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        print("Testing deposit...")
        self.assertEqual(account.get_balance(), 100)
        print(f"Balance after deposit: {account.get_balance()}")
    
    def test_withdraw(self):
        account = BankAccount()
        account.deposit(200)
        account.withdraw(50)
        print("Testing withdrawal...")
        self.assertEqual(account.get_balance(), 150)
        print(f"Balance after withdrawal: {account.get_balance()}")
    
    def test_withdraw_more_than_balance(self):
        account = BankAccount()
        account.deposit(100)
        account.withdraw(150)
        print("Testing withdrawal more than balance...")
        self.assertEqual(account.get_balance(), 100)  # Balance should not go below initial deposit
        print(f"Balance after attempting to withdraw more than available: {account.get_balance()}")

if __name__ == "__main__":
    unittest.main()
