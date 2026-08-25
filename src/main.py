from api_client import APIClient
from portfolio import Portfolio
from market import Market

def main():
    api_client = APIClient("https://www.alphavantage.co")
    market = Market(api_client)
    my_portfolio = Portfolio(market)
    while True:
        print("1. Add Stock")
        print("2. Show Portfolio")
        print("3. Show Cash")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            try:
                ticker = input("Ticker : ")
                shares = int(input("Shares : "))
                purchase_price = float(input("Purchase Price : "))
                if shares * purchase_price > my_portfolio.cash:
                    print("Not enough cash to buy this stock.")
                    while True:
                        answer = input("Do you want to buy less shares? (y/n) : ")
                        if answer.lower() == 'y': 
                            max_shares = int(my_portfolio.cash // purchase_price)
                            if max_shares == 0:
                                raise ValueError("You don't have enough cash to buy any shares of this stock.")
                            print(f"You can buy maximum {max_shares} shares.")
                            shares = int(input("Enter the number of shares you want to buy : "))
                            if shares <= 0:
                                print("Invalid number of shares. Please enter a positive integer.")
                                continue
                            if shares * purchase_price <= my_portfolio.cash:
                                break
                            else:
                                print("Not enough cash to buy this stock.")
                        elif answer.lower() == 'n':
                            raise ValueError("Not enough cash to buy this stock.")
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                my_portfolio.add_transaction(ticker, shares, purchase_price)
            except ValueError as e:
                print(e)
        elif choice == 2:
            try:
                my_portfolio.show_portfolio()
            except ValueError as e:
                print(e)
        elif choice == 3:
            my_portfolio.show_cash()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()