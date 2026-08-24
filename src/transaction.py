class Transaction:
    def __init__(self, shares, purchase_price, ticker):
        self.shares = shares
        self.purchase_price = purchase_price
        self.ticker = ticker
    def invested(self):
        return self.shares * self.purchase_price
    def curr_value(self, current_price):
        return self.shares * current_price
    def profit(self, current_price):
        return self.curr_value(current_price) - self.invested()
    def return_percent(self, current_price):
        return (self.profit(current_price) / self.invested()) * 100