# Binance Futures Testnet Trading Bot

A lightweight Python CLI trading bot for placing MARKET, LIMIT, and STOP-LIMIT orders on the Binance Futures Testnet.

---

## Overview

This project is a command-line trading bot built in Python that interacts with the **Binance Futures Testnet (USDT-M)**. It allows users to place trading orders directly from the terminal while demonstrating how to structure a small but maintainable Python project.

The application emphasizes **clean code organization, input validation, logging, and error handling**, making it easy to extend with additional trading functionality in the future.

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Place **STOP-LIMIT orders (bonus feature)**
* Supports both **BUY** and **SELL** sides
* Command-line interface using `argparse`
* Input validation for symbol, order type, quantity, and price
* Structured logging for API requests, responses, and errors
* Modular and reusable project architecture

The **STOP-LIMIT order type** is implemented as a **bonus feature beyond the core task requirements**.

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py           # Binance client configuration
│   ├── orders.py           # Order execution logic
│   ├── validators.py       # CLI input validation
│   └── logging_config.py   # Logging configuration
│
├── logs/
│   └── trading_bot.log     # Application logs
│
├── sample_logs/
│   └── trading_bot.log     # Example logs for submission
│
├── cli.py                  # CLI entry point
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup

### 1. Clone the repository

```
git clone <your-repo-url>
cd trading_bot
```

### 2. Create a virtual environment

```
python -m venv venv
```

Activate the environment.

**Windows**

```
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## API Configuration

Create a `.env` file in the project root and add your Binance Testnet API credentials:

```
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

You can generate API keys from:

```
https://testnet.binancefuture.com
```

These keys are used for **Binance Futures Testnet**, so no real funds are involved.

---

## Usage

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 90000
```

### STOP-LIMIT Order (Bonus)

```
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --qty 0.002 --price 120000 --stop 130000
```

Explanation:

* `stop` → trigger price
* `price` → limit price placed after the trigger

---

## Example Output

```
Order Request
-------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

Order Response
--------------
Order ID: 123456789
Status: FILLED
Executed Qty: 0.002
Avg Price: 61234.50

SUCCESS: Order executed successfully
```

---

## Logging

All API requests, responses, and errors are written to:

```
logs/trading_bot.log
```

Example log entry:

```
INFO Sending MARKET order | BTCUSDT BUY qty=0.002
INFO Order response: {...}
```

Logs help track order activity and simplify debugging when interacting with external APIs.

A **sample log file** is included in:

```
sample_logs/trading_bot.log
```

This demonstrates successful execution of MARKET and LIMIT orders as required by the assignment.

---

## Requirements

Dependencies used in this project:

* python-binance
* python-dotenv

Install them with:

```
pip install -r requirements.txt
```

---

## Notes

* Binance Futures Testnet requires a **minimum notional value of 100 USDT** per order.
* LIMIT orders may remain in `NEW` status if the price is far from the current market price.
* STOP-LIMIT orders require a valid trigger (`stop`) and limit (`price`) configuration.
* The project runs on the **Binance Futures Testnet environment**, meaning no real funds are used.

---

## Disclaimer

This project is created for **learning and demonstration purposes only**.
It should not be used for real trading without implementing proper trading strategies, risk management, and production-grade safeguards.
