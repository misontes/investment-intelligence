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
if __name__ == "__main__":
    main()