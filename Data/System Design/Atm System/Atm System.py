'''
#### Name:  Atm System
Link: [link]()


1) User may want to see balance
2) Deposit Cash
3) Withdraw Cash
'''

class ATM:
    states = [ready, enter_pin, select_transcation, deposit, withdraw, display_balance
    dispense_cash, incorrect_pin, no_cash]

    def read_card(): pass

    def authenticate_pin(): pass   # Get account

    def select_transaction(): pass

    def deposit_cash():
        Account.update_balance()

    def withdraw_cash():
        Account.update_balance()

    
    def display_balance(): pass





class User:
    card = 134132
    account = 24324

    get_account(): pass


class Account:
    balance = 234132

    def get_balance():pass
    
    def upadate_balance():pass

class Card:
    def authenticate(): pass



# class Cash:
#     def is_valid(): pass
