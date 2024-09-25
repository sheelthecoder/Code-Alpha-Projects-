import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, symbol, shares):
        """
        Add the specified number of shares of a stock to the portfolio.
        symbol: Ticker symbol of the stock (e.g., 'RELIANCE.NS' for Reliance).
        shares: Number of shares to add.
        """
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")
    
    def remove_stock(self, symbol, shares):
        """
        Remove the specified number of shares of a stock from the portfolio.
        symbol: Ticker symbol of the stock.
        shares: Number of shares to remove. The stock must exist in the portfolio.
        """
        if symbol in self.stocks:
            if self.stocks[symbol] >= shares:
                self.stocks[symbol] -= shares
                if self.stocks[symbol] == 0:
                    del self.stocks[symbol]
                print(f"Removed {shares} shares of {symbol}.")
            else:
                print(f"Cannot remove {shares} shares of {symbol}. Only {self.stocks[symbol]} available.")
        else:
            print(f"{symbol} not found in portfolio.")
    
    def get_current_price(self, symbol):
        """
        Get the current price of a stock using yfinance.
        symbol: Ticker symbol of the stock.
        Returns: The latest stock price or None if the API call fails or data is empty.
        """
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period='1d')  # Fetch today's data
            if not data.empty:
                current_price = data['Close'].iloc[-1]  # Get the latest closing price
                return current_price
            else:
                print(f"No data available for {symbol}.")
                return None
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None
    
    def track_performance(self):
        """
        Track the performance of the stocks in the portfolio by fetching the current price.
        Returns a dictionary containing stock performance data.
        """
        performance = {}
        for symbol, shares in self.stocks.items():
            current_price = self.get_current_price(symbol)
            if current_price is not None:
                performance[symbol] = {
                    'shares': shares,
                    'current_price': current_price,
                    'total_value': shares * current_price
                }
        return performance

def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. Track Performance\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            # User should input a stock ticker symbol like 'RELIANCE.NS', 'TCS.NS', or '^NSEI'
            symbol = input("Enter stock symbol (e.g., RELIANCE.NS for Reliance, ^NSEI for Nifty 50): ")
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)

        elif choice == '2':
            # User should input the ticker symbol of the stock they wish to remove
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(symbol, shares)

        elif choice == '3':
            # Track the current performance of all stocks in the portfolio
            performance = portfolio.track_performance()
            df = pd.DataFrame(performance).T  # Transpose DataFrame for better display
            if not df.empty:
                print("\nCurrent Portfolio Performance:")
                print(df)
            else:
                print("No data to display.")

        elif choice == '4':
            # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
