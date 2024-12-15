# Dynamic Stock Scanner

## Overview
The Dynamic Stock Scanner is a Python-based tool designed to fetch historical stock data and analyze stock returns over a specified period. It allows users to dynamically set thresholds for return percentages and schedules the scanner to run daily at a specific time. This project is ideal for investors and analysts who want to identify stocks meeting specific return criteria.

## Features
- Fetches historical stock data using the Yahoo Finance API.
- Calculates percentage returns over a user-specified time frame.
- Filters stocks based on a dynamically set return threshold.
- Schedules daily scans to run automatically at a specified time.
- Easy-to-use interactive input for return thresholds and time periods.

## Requirements
To run this project, ensure you have the following dependencies installed:
- Python 3.7+
- `yfinance`
- `pandas`
- `schedule`

Install dependencies using:
```bash
pip install yfinance pandas schedule
```

## Usage

### Running the Scanner
1. Clone the repository or copy the script to your local environment.
2. Run the script using Python:
   ```bash
   python dynamic_stock_scanner.py
   ```
3. Enter the desired return threshold (e.g., 0 for 0% return) and the number of years for historical analysis when prompted.
4. The script will:
   - Fetch data for specified stocks (e.g., `AAPL`, `MSFT`, `GOOGL`).
   - Calculate their percentage returns over the specified period.
   - Display stocks meeting the criteria.

### Scheduled Execution
The scanner is set to run daily at 6:00 PM by default. This can be adjusted in the script by modifying the line:
```python
schedule.every().day.at("18:00").do(run_scanner)
```

### Example Output
```
Enter return threshold (e.g., 0 for 0%): 0
Enter number of years: 7
Stocks meeting criteria: [('AAPL', -0.05), ('MSFT', 0.02)]
Stocks with 0% return: []
```

## Functions

### `get_stock_data(stock_symbol, years)`
Fetches historical stock data for a given symbol and period.
- **Parameters:**
  - `stock_symbol` (str): The ticker symbol of the stock (e.g., `AAPL`).
  - `years` (int): Number of years of data to fetch.
- **Returns:** A Pandas DataFrame of historical stock data.

### `calculate_return(stock_data)`
Calculates the return percentage based on the stock’s initial and final closing prices.
- **Parameters:**
  - `stock_data` (DataFrame): Historical stock data.
- **Returns:** Return percentage (float).

### `stock_scanner(stocks, return_threshold, years)`
Filters stocks based on return threshold over a specified time period.
- **Parameters:**
  - `stocks` (list): List of stock ticker symbols.
  - `return_threshold` (float): Desired return percentage.
  - `years` (int): Number of years for analysis.
- **Returns:** A list of stocks meeting the criteria.

### `run_scanner()`
Runs the scanner for predefined stocks and logs results.

## Customization
- **Add More Stocks:** Update the `stocks_to_check` list in the `run_scanner` function with additional stock symbols.
- **Change Schedule Time:** Modify the scheduled time in the `schedule.every().day.at()` function.

## Limitations
- The script relies on Yahoo Finance data, which may have occasional outages or limitations.
- The return threshold uses absolute percentage values and may require further refinement for complex strategies.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

## Contributing
Contributions are welcome! Submit an issue or a pull request to enhance the functionality or fix bugs.

## Acknowledgments
- [Yahoo Finance API](https://pypi.org/project/yfinance/) for providing financial data.
- [Schedule Library](https://pypi.org/project/schedule/) for enabling easy scheduling.

---

Start scanning stocks dynamically and uncover new investment opportunities with this script! 🚀

