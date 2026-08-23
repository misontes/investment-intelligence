class Market:
    def __init__(self):
        pass
    def get_price(self, ticker):
        import random
        return round(random.uniform(10, 100), 2)
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

class Portfolio:
    def __init__(self):
        self.portfolio = {}
        self.cash = 10000.0  # Starting cash balance
    def get_price(self, ticker):
        return Market().get_price(ticker)
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
                print(f"Shares: {transaction.shares}, Purchase Price: {transaction.purchase_price}, Current Price: {current_price[ticker]}, Invested: {transaction.invested()}, Current Value: {transaction.curr_value(current_price[ticker])}, Profit: {transaction.profit(current_price[ticker])}, Return: {transaction.return_percent(current_price[ticker])}%")
    def show_cash(self):
        print(f"Cash Balance: {self.cash}")
my_portfolio = Portfolio()

def main():
    while True:
        print("1. Add Stock")
        print("2. Show Portfolio")
        print("3. Show Cash")
        print("4. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            my_portfolio.add_transaction()
        elif choice == 2:
            my_portfolio.show_portfolio()
        elif choice == 3:
            my_portfolio.show_cash()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

main()