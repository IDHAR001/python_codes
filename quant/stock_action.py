class account():
    def __init__(self, wallet_name, stock_total_amounts, wallet_balance):
        self.wallet_name = wallet_name
        self.stock_total_amounts = stock_total_amounts
        self.wallet_balance = wallet_balance

def buy_stock(account, stock_amounts, unit_price):
    account.stock_total_amounts += stock_amounts
    account.wallet_balance -= unit_price*stock_amounts

def sell_stock(account, stock_amounts, unit_price):
    account.stock_total_amounts += stock_amounts
    account.wallet_balance += unit_price*stock_amounts

def sell_all_stock(account, unit_price):
    account.wallet_balance += unit_price*(account.stock_total_amounts)
    account.stock_total_amounts = 0