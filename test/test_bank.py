class BankAccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def deposit(self, amount):
        self.balance += amount
        return True
    
def test_insufficient_deposit():
    a = BankAccount(1)
    a.deposit(100)
    outcome = a.withdraw(150)
    assert outcome  == False