# 📈 Stock Dashboard

A powerful command-line stock market dashboard built with Python. Track real-time stock prices, set price alerts, manage watchlists, and visualize historical data with beautiful charts.

## ✨ Features

- 🔍 **Real-time Stock Data** - Get current prices, market cap, volume, and price changes
- 📊 **Multi-Stock Comparison** - Compare multiple stocks side-by-side with color-coded performance
- 📌 **Watchlist Management** - Save and quickly check your favorite stocks
- 🔔 **Price Alerts** - Set alerts for price targets (above/below thresholds)
- 📉 **Historical Charts** - Visualize stock performance over various time periods
- 📈 **Comparison Charts** - Compare normalized performance of multiple stocks
- 💾 **Persistent Storage** - Watchlists and alerts saved between sessions
- 🎨 **Beautiful UI** - Color-coded terminal output for easy reading

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**
```bash
git clone 
cd stock_dashboard
```

2. **Install required packages**
```bash
pip install yfinance matplotlib
```

3. **Run the application**
```bash
python main.py
```

## 📖 Usage

### Main Menu

When you run the application, you'll see the main menu with the following options:
```
Stock Dashboard - Main Menu
==================================================
1.  Check specific stocks
2.  Check watchlist
3.  Add to watchlist
4.  Remove from watchlist
5.  View watchlist
6.  Set price alert
7.  View alerts
8.  Remove alert
9.  Show historical chart
10. Compare stocks chart
11. Exit
==================================================
```

### 1. Check Specific Stocks

Enter one or more stock tickers (comma-separated) to view current data:
```
Enter stock tickers (comma-separated): AAPL, TSLA, GOOGL
```

**Output:**
```
Ticker   Company                          Price        Change               Market Cap     
------------------------------------------------------------------------------------------
AAPL     Apple Inc.                       $175.43      ▲ $2.15 (+1.24%)     $2.7T
TSLA     Tesla, Inc.                      $242.84      ▼ $5.32 (-2.14%)     $771.2B
GOOGL    Alphabet Inc. Class A            $139.57      ▲ $0.89 (+0.64%)     $1.8T
```

### 2. Manage Watchlist

**Add stocks to watchlist:**
- Choose option `3`
- Enter tickers: `AAPL, MSFT, NVDA`

**View watchlist:**
- Choose option `5`

**Check all watchlist stocks:**
- Choose option `2` (displays current data for all saved stocks)

**Remove from watchlist:**
- Choose option `4`
- Enter tickers to remove

### 3. Set Price Alerts

**Create an alert:**
- Choose option `6`
- Enter ticker: `AAPL`
- Enter target price: `180`
- Choose alert type: `above` or `below`

The system will notify you when checking stocks if any alerts are triggered! 🔔

**View all alerts:**
- Choose option `7`

**Remove alerts:**
- Choose option `8`
- Enter ticker and alert index (or leave empty to remove all)

### 4. Visualize Historical Data

**Single stock chart:**
- Choose option `9`
- Enter ticker: `TSLA`
- Choose period: `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, or `max`

**Compare multiple stocks:**
- Choose option `10`
- Enter tickers: `AAPL, MSFT, GOOGL`
- Choose period

The comparison chart shows normalized performance (percentage change from start).

## 📁 Project Structure
```
stock_dashboard/
├── main.py                # Main program entry point
├── stock_dashboard.py     # Core stock data & chart functions
├── alert.py               # Alert management functions
├── watchlist.py           # Watchlist management functions
├── watchlist.json         # Auto-generated watchlist data
├── alerts.json            # Auto-generated alerts data
└── README.md              # This file
```

## 🛠️ Technical Details

### Dependencies

- **yfinance** - Fetch real-time and historical stock data from Yahoo Finance
- **matplotlib** - Create beautiful charts and visualizations
- **json** - Store watchlists and alerts persistently
- **os** - File system operations

### Data Sources

Stock data is fetched from Yahoo Finance via the `yfinance` library. This includes:
- Real-time stock prices
- Historical price data
- Company information
- Market statistics

### File Storage

- `watchlist.json` - Stores your saved stock tickers
- `alerts.json` - Stores price alerts with target prices and conditions

## 💡 Examples

### Example 1: Daily Stock Check Routine
```
1. Run: python main.py
2. Choose option 2 (Check watchlist)
3. Review your stocks and any triggered alerts
4. Update alerts if needed
```

### Example 2: Research Before Investment
```
1. Choose option 1 (Check specific stocks)
2. Enter: AAPL, MSFT, GOOGL, NVDA, TSLA
3. Choose option 10 (Compare stocks chart)
4. Enter same tickers with period: 1y
5. Analyze the normalized performance chart
```

### Example 3: Set Up Monitoring
```
1. Choose option 3 (Add to watchlist)
2. Enter: AAPL, TSLA, NVDA
3. Choose option 6 (Set price alert)
4. Set alert: AAPL above $180
5. Set alert: TSLA below $200
6. Now option 2 will monitor and notify you!
```

## 🎨 Features in Detail

### Color-Coded Display

- 🟢 **Green** - Positive price changes
- 🔴 **Red** - Negative price changes
- 🔵 **Cyan** - Headers and informational text
- 🟡 **Yellow** - Warnings and triggered alerts

### Time Periods Available

- `1d` - 1 day
- `5d` - 5 days
- `1mo` - 1 month (default)
- `3mo` - 3 months
- `6mo` - 6 months
- `1y` - 1 year
- `2y` - 2 years
- `5y` - 5 years
- `max` - Maximum available history

## 🔧 Customization

You can easily customize the dashboard:

1. **Change color scheme** - Edit color codes in `stock_dashboard.py`
2. **Modify display format** - Update `display_comparison()` function
3. **Add new features** - Each module is independent and easy to extend
4. **Adjust chart styling** - Modify matplotlib settings in chart functions

## 🐛 Troubleshooting

### Issue: "No data available"
- **Solution**: Check if the ticker symbol is correct
- **Solution**: Verify internet connection
- **Solution**: Some tickers may have limited data on Yahoo Finance

### Issue: Charts not displaying
- **Solution**: Ensure matplotlib is installed: `pip install matplotlib`
- **Solution**: On some systems, you may need additional GUI backend

### Issue: Price showing as $0.00
- **Solution**: The market might be closed
- **Solution**: Try using `previousClose` data
- **Solution**: Verify the ticker is actively traded

## 📝 To-Do / Future Enhancements

- [ ] Add portfolio tracking with cost basis
- [ ] Export data to CSV/Excel
- [ ] Email notifications for alerts
- [ ] Technical indicators (RSI, MACD, Moving Averages)
- [ ] News feed integration
- [ ] Sector performance comparison
- [ ] Real-time streaming updates
- [ ] Web interface (Flask/Django)
- [ ] Mobile app version

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - feel free to use it for personal or commercial projects.

## ⚠️ Disclaimer

This tool is for informational purposes only. It is not financial advice. Always do your own research before making investment decisions. Stock prices and data are provided by Yahoo Finance and may be delayed.

## 👨‍💻 Author

Created as a learning project to practice Python programming, API integration, data visualization, and building useful command-line tools.

## 🙏 Acknowledgments

- **yfinance** - For providing easy access to Yahoo Finance data
- **matplotlib** - For powerful charting capabilities
- **Yahoo Finance** - For stock market data

---

**Happy Trading! 📈💰**