
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] Holder: {self.account_holder}, Balance: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self.balance -= amount


class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, lock_in_period=12):
        super().__init__(account_number, account_holder, balance)
        self.lock_in_period = lock_in_period
        self.months_elapsed = 0

    def withdraw(self, amount):
        if self.months_elapsed < self.lock_in_period:
            raise ValueError("Cannot withdraw before lock-in period ends")
        super().withdraw(amount)

    def pass_month(self):
        self.months_elapsed += 1


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer_funds(self, from_acc, to_acc, amount):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            raise ValueError("One or both accounts not found")
        self.accounts[from_acc].withdraw(amount)
        self.accounts[to_acc].deposit(amount)


# Test Program
if __name__ == "__main__":
    bank = Bank()

    # 1. Create accounts
    s_acc = SavingsAccount("S123", "Alice", 1000, 0.05)
    c_acc = CurrentAccount("C456", "Bob", 500, 300)
    f_acc = FixedDepositAccount("F789", "Charlie", 2000, lock_in_period=6)

    bank.add_account(s_acc)
    bank.add_account(c_acc)
    bank.add_account(f_acc)

    print("=== Initial Accounts ===")
    print(s_acc)
    print(c_acc)
    print(f_acc)

    # 2. SavingsAccount test
    print("\n=== Savings Account Test ===")
    s_acc.deposit(500)
    print("After deposit:", s_acc)
    s_acc.apply_interest()
    print("After applying interest:", s_acc)

    # 3. CurrentAccount test
    print("\n=== Current Account Test ===")
    print("Before withdrawal:", c_acc)
    c_acc.withdraw(700)  # within overdraft limit
    print("After withdrawal:", c_acc)

    # 4. FixedDepositAccount test
    print("\n=== Fixed Deposit Account Test ===")
    print("Attempting early withdrawal...")
    try:
        f_acc.withdraw(500)
    except ValueError as e:
        print("Error:", e)

    print("Simulating 6 months...")
    for _ in range(6):
        f_acc.pass_month()

    f_acc.withdraw(500)
    print("After lock-in withdrawal:", f_acc)

    # 5. Bank transfer test
    print("\n=== Bank Transfer Test ===")
    print("Before transfer:")
    print(s_acc)
    print(c_acc)

    bank.transfer_funds("S123", "C456", 200)

    print("After transfer:")
    print(s_acc)
    print(c_acc)
