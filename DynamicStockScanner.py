import yfinance as yf
import pandas as pd
import schedule
import time

# Function to fetch historical data for a stock
def get_stock_data(stock_symbol, years):
    # Calculate start date based on the number of years
    end_date = pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(years=years)
    
    # Fetch historical data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

# Example usage
data = get_stock_data('AAPL', 7)  # Fetch 7 years of Apple stock data
print(data.head())

def calculate_return(stock_data):
    # Get first and last closing prices
    initial_price = stock_data['Close'].iloc[0]
    final_price = stock_data['Close'].iloc[-1]
    
    # Calculate return percentage
    return_percent = ((final_price - initial_price) / initial_price) * 100
    return return_percent

def stock_scanner(stocks, return_threshold=0, years=7):
    results = []
    
    for stock in stocks:
        stock_data = get_stock_data(stock, years)
        
        if not stock_data.empty:
            return_percent = calculate_return(stock_data)
            
            if abs(return_percent - return_threshold) < 0.1:  # Allow for minor floating-point differences
                results.append((stock, return_percent))
    
    return results


def run_scanner():
    stocks_to_check = ['AAPL', 'MSFT', 'GOOGL']  # Add more symbols as needed
    results = stock_scanner(stocks_to_check, return_threshold=0, years=7)
    print(f'Stocks with 0% return: {results}')


return_threshold = float(input("Enter return threshold (e.g., 0 for 0%): "))
years = int(input("Enter number of years: "))

# Run the scanner with user-provided values
results = stock_scanner(['AAPL', 'MSFT', 'GOOGL'], return_threshold=return_threshold, years=years)
print(f'Stocks meeting criteria: {results}')

# Schedule the scanner to run at 6:00 PM daily
schedule.every().day.at("18:00").do(run_scanner)

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute