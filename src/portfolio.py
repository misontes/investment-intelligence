from market import Market
import market
from transaction import Transaction
class Portfolio:
    def __init__(self, market):
        self.portfolio = {}
        self.cash = 10000.0  
        self.market = market
    def get_price(self, ticker):
        return self.market.get_price(ticker)
    def add_transaction(self, ticker, shares, purchase_price):
        if shares <= 0:
            raise ValueError("Shares must be positive.")
        if purchase_price <= 0:
            raise ValueError("Purchase price must be positive.")
        self.get_price(ticker)
        if shares * purchase_price > self.cash:
            raise ValueError("Insufficient cash to complete the transaction.")
        transaction = Transaction(shares, purchase_price, ticker)
        if ticker not in self.portfolio:
            self.portfolio[ticker] = []
        self.portfolio[ticker].append(transaction)
        self.cash -= shares * purchase_price
    def show_portfolio(self):
        current_price = {}
        total_invested = 0
        total_current_value = 0
        total_profit = 0
        total_return = 0
        total_portfolio_value = 0
        for ticker, transactions in self.portfolio.items():
            curr_price_for_ticker = self.get_price(ticker)
            current_price[ticker] = curr_price_for_ticker
            print(f"Ticker: {ticker}")
            for transaction in transactions: 
                total_invested += transaction.invested()
                total_current_value += current_price[ticker] * transaction.shares
                total_profit += transaction.profit(current_price[ticker])
                total_return += transaction.return_percent(current_price[ticker])
                print(f"Shares: {transaction.shares}\n Purchase Price: {transaction.purchase_price}\n Current Price: {current_price[ticker]}\n Invested: {transaction.invested()}\n Current Value: {transaction.curr_value(current_price[ticker])}\n Profit: {transaction.profit(current_price[ticker])}\n Return: {transaction.return_percent(current_price[ticker])}%\n\n")
        total_portfolio_value = total_current_value + self.cash
        print("-" * 40)
        print(f"Total invested: {total_invested}")
        print(f"Total current value: {total_current_value}")
        print(f"Total profit: {total_profit}")
        print(f"Total return: {total_return:.2f}%")
        print(f"Cash available: ${self.cash:.2f}")
        print(f"Total portfolio value: ${total_portfolio_value:.2f}")
        print("-" * 40)
    def show_cash(self):
        print(f"Cash available: ${self.cash:.2f}")