import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime


# Get current date and time
now = datetime.now()

# ANSI color codes for terminal
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'

def get_stock_data(ticker):
	try:
		stock = yf.Ticker(ticker)
		info = stock.info

		# Get current and previous price
		current_price = info.get('currentPrice', 0)
		previous_price = info.get('previousClose', 0)

		# Calculate price change
		# check if both values exist and are not zero/None/empty
		if previous_price and current_price:
			price_change = current_price - previous_price
			percent_change = (price_change / previous_price) * 100

			# Choose color based on change
			if price_change >= 0:
				color = GREEN
				arrow = "▲"
			else:
				color = RED
				arrow = "▼"
		else:
			price_change = 0
			percent_change = 0
			color = RESET
			arrow = '-'

		# Truncate long name with ellipsis
		longname = info.get('longName', 'N/A')
		if len(longname) > 28:
			company_name = longname[:28] + '...'
		else:
			company_name = longname

		return {'ticker': ticker,
				'name': company_name,
				'price': current_price,
				'color': color,
				'arrow': arrow,
				'change': price_change,
				'percent': percent_change,
				'market_cap': info.get('marketCap', 0)}
	except Exception as e:
		print(f"{RED}Error fetching {ticker}: {e}{RESET}")
		return None


def display_comparison(stocks_data):
	"""Display multiple stocks in a comparison table"""
	print(f"\nUpdated: {now.strftime('%B %d, %Y at %I:%M %p')}")
	# Output: Updated: November 29, 2025 at 02:30 PM
	print(f"{CYAN}{'='*90}{RESET}")
	print(f"{BOLD}{CYAN}Stock Dashboard - Multi-Stock Comparison{RESET}")
	print(f"{CYAN}{'='*90}{RESET}")

	# Header
	print(f"{BOLD}{'Ticker':<8} {'Company':<30} {'Price':<12} {'Change':<22} {'Market Cap':<15}{RESET}")
	print(f"{'-'*90}")

	# Display each stock
	for data in stocks_data:
		if data:
			print(f"{data['ticker']:<8}"
				  f"{data['name']:<32}"
				  f"{data['price']:<12}"
				  f"{data['color']}{data['arrow']} $ {data['change']:<+6.2f} ( {data['percent']:>+6.2f}%){RESET:<8}"
				  f"${data['market_cap']/1e9:>6.1f}B")

	print(f"{CYAN}{'='*90}{RESET}")

def check_stocks(tickers):
	"""Check stocks and display data"""
	print(f"\n{CYAN}Fetching data....{RESET}")
	stocks_data = []

	for ticker in tickers:
		data = get_stock_data(ticker)
		if data:
			stocks_data.append(data)

	if stocks_data:
		display_comparison(stocks_data)
	else:
		print(f"{RED}No valid stocks data found.{RESET}")

def plot_historical_chart(ticker, period='1mo'):
	"""
	Plot historical price chart for a stock

	Args:
	    ticker: Stock ticker symbol
	    period: Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max)
	"""
	try:
		ticker = ticker.upper().strip()
		stock = yf.Ticker(ticker)

		# Get historical data
		hist = stock.history(period=period)

		if hist.empty:
			print(f"{RED}No historical data available for {ticker}{RESET}")
			return
		
		# Create the plot
		plt.figure(figsize=(12, 6))
		plt.plot(hist.index, hist['Close'], linewidth=2, color='#1f77b4')
		plt.fill_between(hist.index, hist['Close'], alpha=0.3, color='#1f77b4')

		# Formatting
		plt.title(f'{ticker} - Historical Price Chart ({period})', fontsize=16, fontweight='bold')
		plt.xlabel('Date', fontsize=12)
		plt.ylabel('Price (USD)', fontsize=12)
		plt.grid(True, alpha=0.3)
		plt.xticks(rotation=45)
		plt.tight_layout()

		# Add current price annotation
		current_price = hist['Close'].iloc[-1]
		plt.axhline(y=current_price, color='r', linestyle='--', alpha=0.5, label=f'Current: ${current_price:.2f}')
		plt.legend()

		print(f"{GREEN}Displaying chart for {ticker}: {e}{RESET}")
		plt.show()

	except Exception as e:
		print(f"{RED}Error plotting chart for {ticker}: {e}{RESET}")

def plot_comparison_chart(tickers, period='1mo'):
	"""
	Args:
	    tickers: List of stock ticker symbols
		period: Time period (1d, 5, 1mo, 3mo, 6mo, 1y, 2y, 5y, max)
	"""
	try:
		plt.figure(figsize=(14, 7))

		for ticker in tickers:
			ticker = ticker.upper().strip()
			stock = yf.Ticker(ticker)
			hist = stock.history(period=period)

			if not hist.empty:
				# Normalize to percentage change from start
				normalized = (hist['Close'] / hist['Close'].iloc[0] -1) * 100
				plt.plot(normalized.index, normalized, linewidth=2, label=ticker, marker='o', markersize=3)
		
		# Formatting
		plt.title(f'Stock Comparison - Normalized Performance ({period})', fontsize=16, fontweight='bold')
		plt.xlabel('Date', fontsize=12)
		plt.ylabel('Percentage Change (%)', fontsize=12)
		plt.grid(True, alpha=0.3)
		plt.legend(fontsize=10)
		plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
		plt.xticks(rotation=45)
		plt.tight_layout()

		print(f"{GREEN}Displaying comparison chart...{RESET}")
		plt.show()

	except Exception as e:
		print(f"{RED}Error plotting comparison chart: {e}{RESET}")
	



