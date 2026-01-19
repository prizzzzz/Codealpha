# Task 2: Stock Portfolio Tracker

A comprehensive stock portfolio management system with buy/sell functionality.

## 📊 Features

- **Stock Database**: Pre-loaded with 10 popular stocks (AAPL, TSLA, GOOGL, MSFT, AMZN, META, NFLX, NVDA, JPM, V)
- **Buy Stocks**: Add stocks to your portfolio with quantity tracking
- **Sell Stocks**: Remove stocks from your portfolio with validation
- **Portfolio View**: Display current holdings with company names
- **Portfolio Summary**: Calculate total investment value
- **Save/Load**: Save portfolio to JSON file and load it later
- **Error Handling**: Validates inputs and handles edge cases

## 📈 Available Stocks

| Symbol | Company Name | Price/Share |
|--------|-------------|-------------|
| AAPL   | Apple Inc. | $180.50 |
| TSLA   | Tesla Inc. | $250.75 |
| GOOGL  | Alphabet Inc. | $140.25 |
| MSFT   | Microsoft Corporation | $380.00 |
| AMZN   | Amazon.com Inc. | $170.80 |
| META   | Meta Platforms Inc. | $350.60 |
| NFLX   | Netflix Inc. | $240.30 |
| NVDA   | NVIDIA Corporation | $875.90 |
| JPM    | JPMorgan Chase & Co. | $155.40 |
| V      | Visa Inc. | $280.20 |

## 🚀 How to Run

```bash
cd Task2_StockTracker
python stock_tracker.py
```

## 📋 Menu Options

1. **Buy stocks** - Add stocks to your portfolio
2. **Sell stocks** - Remove stocks from your portfolio
3. **View portfolio** - See your current holdings
4. **View portfolio summary** - Calculate total value
5. **Save portfolio to file** - Export to JSON
6. **Load portfolio from file** - Import from JSON
7. **Exit** - Close the application

## 💡 Usage Example

```
STOCK PORTFOLIO TRACKER
======================================================================

Available stocks:
Symbol   Company Name                   Price/Share    
----------------------------------------------------------------------
AAPL     Apple Inc.                     $180.50        
TSLA     Tesla Inc.                     $250.75        
...

PORTFOLIO MENU
======================================================================
1. Buy stocks
2. Sell stocks
3. View portfolio
4. View portfolio summary
5. Save portfolio to file
6. Load portfolio from file
7. Exit

Enter your choice (1-7): 1
Enter stock symbol to buy: AAPL
Enter quantity for AAPL: 10
✅ Bought 10 share(s) of AAPL at $180.50 each
   Total cost: $1805.00
```

## 🔧 Requirements

- Python 3.6+
- Standard library only (uses `json` and `datetime`)

## 📦 Files

- `stock_tracker.py` - Main application file
- `README.md` - This documentation

## 💾 Data Storage

Portfolios are saved as JSON files with the following structure:
```json
{
  "timestamp": "2024-01-15T14:30:45",
  "portfolio": {
    "AAPL": 10,
    "TSLA": 5
  },
  "total_value": 3055.25
}
```

## 💡 Code Features

- Clean, well-documented code
- Input validation and error handling
- JSON file persistence
- User-friendly interface
- Follows Python PEP 8 style guidelines
