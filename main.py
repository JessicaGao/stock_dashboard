from watchlist import *
from stock_dashboard import *

## Your Project Structure Now:
"""
stock_dashboard/
├── main.py                # Main program entry point
├── stock_dashboard.py     # Core stock data & chart functions
├── alert.py               # Alert management functions
├── watchlist.py           # Watchlist management functions
├── watchlist.json         # Auto-generated watchlist data
├── alerts.json            # Auto-generated alerts data
└── README.md              # This file
"""

def show_menu():
	"""Display main menu"""
	print(f"\n{BOLD}{CYAN}Stock Dashboard - Main Menu{RESET}")
	print(f"{CYAN}{'='*50}{RESET}")
	print("1. Check specific stocks")
	print("2. Check watchlist")
	print("3. Add to watchlist")
	print("4. Remove from watchlist")
	print("5. View watchlist")
	print("6. Exit")
	print(f"{CYAN}{'='*50}{RESET}")

def main():
	"""Main program loop"""
	while True:
		show_menu()
		choice = input(f"\n{BOLD}Enter your choice (1-6): {RESET}").strip()

		if choice == '1':
			tickers_input = input(f"{BOLD}Enter stock tickers (comma-seperated): {RESET}").upper()
			tickers = [t.strip() for t in tickers_input.split(',')]
			check_stocks(tickers)

		elif choice == '2':
			watchlist = load_watchlist()
			if watchlist:
				check_stocks(watchlist)
			else:
				print(f"{YELLOW}Your watchlist is empty! Add some stocks first.{RESET}")

		elif choice == '3':
			tickers_input = input(f"{BOLD}Enter tickers to add (comma-seperated): {RESET}").upper()
			tickers = [t.strip() for t in tickers_input.split(',')]
			add_to_watchlist(tickers)

		elif choice == '4':
			view_watchlist()
			tickers_input = input(f"{BOLD}Enter tickers to remove (comma-seperated): {RESET}").upper()
			tickers = [t.strip() for t in tickers_input.split(',')]
			remove_from_watchlist(tickers)

		elif choice == '5':
			view_watchlist()

		elif choice == '6':
			print(f"\n{GREEN}Thanks for using Stock Dashboard! 📈{RESET}\n")
			break

		else:
			print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()
