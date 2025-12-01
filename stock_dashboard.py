import yfinance as yf
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





