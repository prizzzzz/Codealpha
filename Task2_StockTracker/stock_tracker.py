"""
================================================================================
TASK 2: STOCK PORTFOLIO TRACKER
================================================================================
A comprehensive stock portfolio management system with buy/sell functionality.
================================================================================
"""

import json
from datetime import datetime

def stock_portfolio_tracker():
    """Enhanced stock portfolio tracker with buy/sell functionality and portfolio management"""
    
    # Expanded stock database with company names
    stock_database = {
        "AAPL": {"price": 180.50, "name": "Apple Inc."},
        "TSLA": {"price": 250.75, "name": "Tesla Inc."},
        "GOOGL": {"price": 140.25, "name": "Alphabet Inc."},
        "MSFT": {"price": 380.00, "name": "Microsoft Corporation"},
        "AMZN": {"price": 170.80, "name": "Amazon.com Inc."},
        "META": {"price": 350.60, "name": "Meta Platforms Inc."},
        "NFLX": {"price": 240.30, "name": "Netflix Inc."},
        "NVDA": {"price": 875.90, "name": "NVIDIA Corporation"},
        "JPM": {"price": 155.40, "name": "JPMorgan Chase & Co."},
        "V": {"price": 280.20, "name": "Visa Inc."}
    }
    
    portfolio = {}
    
    print("=" * 70)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 70)
    print("\nAvailable stocks:")
    print(f"{'Symbol':<8} {'Company Name':<30} {'Price/Share':<15}")
    print("-" * 70)
    for symbol, data in stock_database.items():
        print(f"{symbol:<8} {data['name']:<30} ${data['price']:<14.2f}")
    print()
    
    # Main menu loop
    while True:
        print("\n" + "=" * 70)
        print("PORTFOLIO MENU")
        print("=" * 70)
        print("1. Buy stocks")
        print("2. Sell stocks")
        print("3. View portfolio")
        print("4. View portfolio summary")
        print("5. Save portfolio to file")
        print("6. Load portfolio from file")
        print("7. Exit")
        
        try:
            choice = input("\nEnter your choice (1-7): ").strip()
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        
        if choice == "1":
            # Buy stocks
            stock = input("Enter stock symbol to buy: ").upper().strip()
            if stock not in stock_database:
                print("❌ Stock not found! Please choose from the available stocks.")
                continue
            
            try:
                quantity = int(input(f"Enter quantity for {stock}: "))
                if quantity <= 0:
                    print("❌ Please enter a positive number!")
                    continue
                
                if stock in portfolio:
                    portfolio[stock] += quantity
                else:
                    portfolio[stock] = quantity
                
                price = stock_database[stock]["price"]
                cost = quantity * price
                print(f"✅ Bought {quantity} share(s) of {stock} at ${price:.2f} each")
                print(f"   Total cost: ${cost:.2f}")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "2":
            # Sell stocks
            if not portfolio:
                print("⚠️  Your portfolio is empty!")
                continue
            
            stock = input("Enter stock symbol to sell: ").upper().strip()
            if stock not in portfolio:
                print(f"❌ You don't own any shares of {stock}!")
                continue
            
            try:
                quantity = int(input(f"Enter quantity to sell (you own {portfolio[stock]}): "))
                if quantity <= 0:
                    print("❌ Please enter a positive number!")
                    continue
                if quantity > portfolio[stock]:
                    print(f"❌ You only own {portfolio[stock]} share(s) of {stock}!")
                    continue
                
                portfolio[stock] -= quantity
                if portfolio[stock] == 0:
                    del portfolio[stock]
                
                price = stock_database[stock]["price"]
                revenue = quantity * price
                print(f"✅ Sold {quantity} share(s) of {stock} at ${price:.2f} each")
                print(f"   Total revenue: ${revenue:.2f}")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "3":
            # View portfolio
            if not portfolio:
                print("\n⚠️  Your portfolio is empty!")
            else:
                print("\n" + "=" * 70)
                print("YOUR PORTFOLIO")
                print("=" * 70)
                print(f"{'Stock':<8} {'Company Name':<30} {'Quantity':<12} {'Price/Share':<15}")
                print("-" * 70)
                for stock, quantity in portfolio.items():
                    data = stock_database[stock]
                    print(f"{stock:<8} {data['name']:<30} {quantity:<12} ${data['price']:<14.2f}")
                print("=" * 70)
        
        elif choice == "4":
            # Portfolio summary
            if not portfolio:
                print("\n⚠️  No stocks in portfolio!")
                continue
            
            total_investment = 0
            print("\n" + "=" * 70)
            print("PORTFOLIO SUMMARY")
            print("=" * 70)
            print(f"{'Stock':<8} {'Quantity':<12} {'Price/Share':<15} {'Total Value':<15}")
            print("-" * 70)
            
            for stock, quantity in portfolio.items():
                price = stock_database[stock]["price"]
                value = quantity * price
                total_investment += value
                print(f"{stock:<8} {quantity:<12} ${price:<14.2f} ${value:<14.2f}")
            
            print("-" * 70)
            print(f"{'TOTAL PORTFOLIO VALUE':<35} ${total_investment:<14.2f}")
            print("=" * 70)
        
        elif choice == "5":
            # Save to file
            if not portfolio:
                print("\n⚠️  No stocks in portfolio to save!")
                continue
            
            filename = input("Enter filename (without extension): ").strip()
            if not filename:
                filename = "portfolio"
            filename += ".json"
            
            try:
                portfolio_data = {
                    "timestamp": datetime.now().isoformat(),
                    "portfolio": portfolio,
                    "total_value": sum(portfolio[stock] * stock_database[stock]["price"] 
                                     for stock in portfolio)
                }
                
                with open(filename, "w") as file:
                    json.dump(portfolio_data, file, indent=2)
                
                print(f"✅ Portfolio saved to {filename}")
            except Exception as e:
                print(f"❌ Error saving file: {e}")
        
        elif choice == "6":
            # Load from file
            filename = input("Enter filename (without extension): ").strip()
            if not filename:
                filename = "portfolio"
            filename += ".json"
            
            try:
                with open(filename, "r") as file:
                    portfolio_data = json.load(file)
                    portfolio = portfolio_data.get("portfolio", {})
                    print(f"✅ Portfolio loaded from {filename}")
                    if portfolio_data.get("timestamp"):
                        print(f"   Saved on: {portfolio_data['timestamp']}")
            except FileNotFoundError:
                print(f"❌ File {filename} not found!")
            except json.JSONDecodeError:
                print(f"❌ Error reading file {filename}. Invalid format!")
            except Exception as e:
                print(f"❌ Error loading file: {e}")
        
        elif choice == "7":
            print("\nThanks for using Stock Portfolio Tracker! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    try:
        stock_portfolio_tracker()
    except KeyboardInterrupt:
        print("\n\nExiting...")
