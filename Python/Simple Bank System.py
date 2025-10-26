# https://leetcode.com/problems/simple-bank-system/

# Example 1:
# Input
# ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
# [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
# Output
# [null, true, true, true, false, false]
# Explanation
# Bank bank = new Bank([10, 100, 20, 50, 30]);
# bank.withdraw(3, 10);    // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
#                          // Account 3 has $20 - $10 = $10.
# bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
#                          // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
# bank.deposit(5, 20);     // return true, it is valid to deposit $20 to account 5.
#                          // Account 5 has $10 + $20 = $30.
# bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
#                          // so it is invalid to transfer $15 from it.
# bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.

class Bank:

    def __init__(self, balance: list[int]):
        # Initialize the bank with a list of balances for each account
        # Index 0 → Account 1, Index 1 → Account 2, and so on
        self.balance = balance       

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Transfers 'money' from account1 to account2.
        Returns True if successful, otherwise False.
        """
        
        # Check if either account number is invalid (out of range)
        if (account1 - 1 >= len(self.balance) or account2 - 1 >= len(self.balance)):
            return False
        
        # Check if the sender account has enough balance
        if (self.balance[account1 - 1] < money):
            return False
        
        # Perform transfer: subtract from sender, add to receiver
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        """
        Deposits 'money' into the specified account.
        Returns True if successful, otherwise False.
        """
        
        # Check if account number is valid
        if (account - 1 >= len(self.balance)):
            return False
        
        # Add the deposit amount to the account balance
        self.balance[account - 1] += money

        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        """
        Withdraws 'money' from the specified account.
        Returns True if successful, otherwise False.
        """
        
        # Check if account number is valid
        if (account - 1 >= len(self.balance)):
            return False
        
        # Check if sufficient funds are available
        if (self.balance[account - 1] < money):
            return False
        
        # Deduct the withdrawal amount from balance
        self.balance[account - 1] -= money
        return True
