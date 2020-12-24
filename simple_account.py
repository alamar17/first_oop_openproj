# Name: Anthony LaMarche
# Description: Simple bank account using object oriented programming

class Account:
    """Class that uses object oriented programming to make a simple bank account."""

    def __init__(self):

        self._accountBalance = 0

    def deposit(self, money):
        # This method of the class account adds a certain value every time it is called to the account balance

        self._accountBalance = self._accountBalance + money

    def withdraw(self, money):

        # This method of class accounts subtracts a certain value every time it is called from the account balance

        if self._accountBalance >= money:

            self._accountBalance -= money
        else:
            return "That is not valid. Please try again."

    def show_balance(self):

        # This method returns the account balance value to the user

        return self._accountBalance
