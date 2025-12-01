from stock_dashboard import (GREEN, RED, RESET, BOLD, CYAN, YELLOW)
import json
import os

WATCHLIST_FILE = 'watchlist.json'

def load_watchlist():
	"""Load watchlist from file"""
	if os.path.exists(WATCHLIST_FILE):
		with open(WATCHLIST_FILE, 'r') as f:
			return json.load(f)
	return []

def save_watchlist(watchlist):
	"""Save watchlist from file"""
	with open(WATCHLIST_FILE, 'w') as f:
		json.dump(watchlist, f)
	print(f"{GREEN}Watchlist saved!{RESET}")

def add_to_watchlist(tickers):
	"""Add tickers to watchlist"""
	watchlist = load_watchlist()
	added = []

	for ticker in tickers:
		ticker = ticker.upper().strip()
		if ticker not in watchlist:
			watchlist.append(ticker)
			added.append(ticker)

	if added:
		save_watchlist(watchlist)
		print(f"{GREEN}Added to watchlist: {', '.join(added)}{RESET}")
	else:
		print(f"{YELLOW}Tickers already in watchlist or invalid{RESET}")

def remove_from_watchlist(tickers):
	"""Remove tickers from watchlist"""
	watchlist = load_watchlist()
	removed = []

	for ticker in tickers:
		ticker = ticker.upper().strip()
		if ticker in watchlist:
			watchlist.remove(ticker)
			removed.append(ticker)

	if removed:
		save_watchlist(watchlist)
		print(f"{GREEN}Removed from watchlist: {', '.join(removed)}{RESET}")
	else:
		print(f"{YELLOW}Tickers not found in watchlist{RESET}")

def view_watchlist():
	"""Display current watchlist"""
	watchlist = load_watchlist()
	if watchlist:
		print(f"\n{CYAN}{'='*50}{RESET}")
		print(f"{BOLD}{CYAN}Your Watchlist{RESET}")
		print(f"{CYAN}{'='*50}{RESET}")
		for i, ticker in enumerate(watchlist, 1):
			print(f"{i}. {ticker}")
		print(f"{CYAN}{'='*50}{RESET}\n")
	else:
		print(f"{YELLOW}Your watchlist is empty!{RESET}")

