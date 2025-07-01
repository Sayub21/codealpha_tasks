# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

def get_user_portfolio():
    portfolio = {}
    print("Enter stock symbols and quantities. Type 'done' when finished.")

    while True:
        symbol = input("Stock Symbol (e.g., AAPL): ").upper()
        if symbol == 'DONE':
            break
        if symbol not in stock_prices:
            print("Symbol not found in price list. Try again.")
            continue
        try:
            quantity = int(input(f"Quantity of {symbol}: "))
            if quantity < 0:
                raise ValueError
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Please enter a valid positive integer for quantity.")
    
    return portfolio

def calculate_total_investment(portfolio):
    total = 0
    print("\nYour Portfolio Summary:")
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = price * quantity
        total += value
        print(f"{symbol}: {quantity} shares × ${price} = ${value}")
    print(f"\nTotal Investment Value: ${total}")
    return total

def save_to_file(portfolio, total, filename="portfolio_summary.csv"):
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for symbol, quantity in portfolio.items():
            price = stock_prices[symbol]
            value = price * quantity
            file.write(f"{symbol},{quantity},{price},{value}\n")
        file.write(f"\nTotal Investment,,,{total}\n")
    print(f"Portfolio saved to '{filename}'.")

def main():
    portfolio = get_user_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total = calculate_total_investment(portfolio)

    save_option = input("Do you want to save the summary to a file? (yes/no): ").lower()
    if save_option == "yes":
        save_to_file(portfolio, total)

if __name__ == "__main__":
    main()
