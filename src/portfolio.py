from transaction import Transaction
class Portfolio:
    def __init__(self, market):
        self.portfolio = {}
        self.cash = 10000.0  
        self.market = market
    def get_price(self, ticker):
        return self.market.get_price(ticker)
    def add_transaction(self):
        ticker = input("Ticker : ")
        shares = int(input("Shares : "))
        purchase_price = float(input("Purchase Price : "))
        if shares * purchase_price > self.cash:
                while True:
                    print("Not enough cash to buy this stock.")
                    answer = input("Do you want to buy less shares? (y/n) : ")
                    if answer.lower() == 'y': 
                        max_shares = int(self.cash // purchase_price)
                        print(f"You can buy maximum {max_shares} shares.")
                        shares = int(input("Enter the number of shares you want to buy : "))
                        if shares * purchase_price <= self.cash:
                            break
                    else:
                        return
        transaction = Transaction(shares, purchase_price, ticker)
        self.cash -= shares * purchase_price
        if ticker not in self.portfolio:
            self.portfolio[ticker] = []
        self.portfolio[ticker].append(transaction)
    def show_portfolio(self):
        current_price = {}
        for ticker, transactions in self.portfolio.items():
            print(f"Ticker: {ticker}")
            current_price[ticker] = self.get_price(ticker)
            for transaction in transactions: 
                print(f"Shares: {transaction.shares}\n, Purchase Price: {transaction.purchase_price}\n, Current Price: {current_price[ticker]}\n, Invested: {transaction.invested()}\n, Current Value: {transaction.curr_value(current_price[ticker])}\n, Profit: {transaction.profit(current_price[ticker])}\n, Return: {transaction.return_percent(current_price[ticker])}%\n")
    def show_cash(self):
        print(f"Cash Balance: {self.cash}")