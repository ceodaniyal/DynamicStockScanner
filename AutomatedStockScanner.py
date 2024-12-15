import yfinance as yf
import pandas as pd

def get_stock_data(stock_symbol, years=10):
    end_date = pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(years=years)
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

# Example usage
data = get_stock_data('AAPL', 10)
print(data.head())

def find_lifetime_high(stock_data):
    lifetime_high = stock_data['High'].max()
    return lifetime_high

def check_support(stock_data, lifetime_high, threshold=0.02, days=5):
    support_days = 0
    for index, row in stock_data.iterrows():
        # Check if price is within 2% of the lifetime high (considered support level)
        if row['Low'] >= lifetime_high * (1 - threshold):
            support_days += 1
            # If price stays near the lifetime high for 'days' consecutive sessions, it's a strong support
            if support_days >= days:
                return True
        else:
            support_days = 0  # Reset if the stock breaks below the threshold
    return False

def check_price_appreciation(stock_data, support_date, appreciation_threshold=0.10):
    support_price = stock_data.loc[support_date]['Low']
    
    # Check for price appreciation from the support price
    for index, row in stock_data.loc[support_date:].iterrows():
        if row['Close'] >= support_price * (1 + appreciation_threshold):
            return True
    return False

def stock_scanner(stocks, years=10, threshold=0.02, days=5, appreciation_threshold=0.10):
    results = []
    
    for stock in stocks:
        stock_data = get_stock_data(stock, years)
        lifetime_high = find_lifetime_high(stock_data)
        
        # Check if the lifetime high is a support level
        if check_support(stock_data, lifetime_high, threshold, days):
            # Check for price appreciation after support test
            support_date = stock_data[stock_data['Low'] >= lifetime_high * (1 - threshold)].index[0]
            if check_price_appreciation(stock_data, support_date, appreciation_threshold):
                results.append((stock, support_date))
    
    return results

# Example usage
stocks_to_scan = ['AAPL', 'MSFT', 'GOOGL']
results = stock_scanner(stocks_to_scan)
print(f'Stocks meeting criteria: {results}')

def analyze_results(results):
    total_instances = len(results)
    annual_opportunities = total_instances / 10  # Since we're analyzing over 10 years
    
    print(f"Total instances found: {total_instances}")
    print(f"Annual opportunities (on average): {annual_opportunities}")
    
    # Assuming we tracked success rate during the scanning process
    successful_trades = sum([1 for result in results if result['success']])  # Define success in your process
    success_rate = (successful_trades / total_instances) * 100
    print(f"Success rate: {success_rate}%")

# Example analysis
if not results :
    print("NO Stocks Meeting the Criteria, hence can't perform analysis")
else :
    analyze_results(results)
