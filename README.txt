High Frequency Trading (HFT) Simulation System
Developed by Anmol Trivedi

IMPORTANT
This project is intended for educational and research purposes only.
It performs paper trading simulation and does not place real market orders. It should not be
used directly for live financial trading without further testing, validation, and regulatory
compliance.

1. INTRODUCTION

This project is a real-time High Frequency Trading (HFT) simulation system developed using
Python and Fyers API WebSocket market data.

The system continuously receives live market ticks, processes microstructure-based trading
signals, evaluates market conditions, applies risk management, and generates paper trading
decisions in real time.

The architecture follows an event-driven trading workflow similar to a basic algorithmic
trading engine.

2. MAIN FEATURES

- Real-time market data streaming using Fyers WebSocket
- Multi-symbol live market monitoring
- Event-driven trading pipeline
- Multiple microstructure-based trading signals
- Weighted signal scoring system
- Buy/Sell confirmation logic
- Cooldown system to prevent overtrading
- Market regime filtering
- Risk management layer
- Paper trading execution
- Stop Loss and Take Profit management
- Position state management
- Duplicate trade prevention
- Realized PnL tracking
- Trade statistics tracking
- CSV trade logging
- Session summary generation
- Colorized terminal monitoring using Colorama
- Debug mode for detailed signal analysis

3. TRADING SIGNALS

The system uses the following market microstructure signals:

1. Order Imbalance
2. Microprice
3. Order Flow
4. Volatility Detection
5. Burst Detection
6. Slippage Detection
7. Liquidity Consumption
8. Absorption Detection
9. Trade Intensity
10. Average Trade Size
11. Spread Analysis

4. PROJECT WORKFLOW

Live Market Data
        |
        v
Tick Processing
        |
        v
Signal Generation
        |
        v
Score Evaluation
        |
        v
Risk Validation
        |
        v
Decision Engine
        |
        v
Paper Trade Execution
        |
        v
Logging & Analytics

5. PROJECT STRUCTURE

HFT_SUBMISSION/
|
|-- auth/
|   |-- auth.py
|   |-- generate_tokens.py
|   `-- testing.py
|
|-- logs/
|   |-- market logs stored here
|
|-- src/
|   |-- core/
|   |   |-- decision_engine.py
|   |   |-- pipeline.py
|   |   |-- score_engine.py
|   |   `-- state_manager.py
|   |
|   |-- data/
|   |   |-- data_adapter.py
|   |   `-- tick_classifier.py
|   |
|   |-- execution/
|   |   `-- order_router.py
|   |
|   |-- live/
|   |   `-- fyers_stream.py
|   |
|   |-- risk/
|   |   |-- regime_detector.py
|   |   `-- risk_manager.py
|   |
|   |-- signals/
|   |   |-- absorption.py
|   |   |-- avg_trade_size.py
|   |   |-- base_signal.py
|   |   |-- burst_detection.py
|   |   |-- liquidity_consumption.py
|   |   |-- microprice.py
|   |   |-- order_flow.py
|   |   |-- order_imbalance.py
|   |   |-- slippage.py
|   |   |-- spread.py
|   |   |-- trade_intensity.py
|   |   `-- volatility.py
|   |
|   `-- utils/
|       |-- config.py
|       `-- logger.py
|
|-- .env.example
|-- requirements.txt

6. SETUP

Prerequisites:
- Python 3.x
- A Fyers trading API account/application
- Valid Fyers API credentials

Install the required Python packages from the project root:

    pip install -r requirements.txt

Configure the environment:

1. Use .env.example as the template for the required environment variables.
2. Create a local .env file.
3. Add your own Fyers API credentials to the .env file.

Do not commit real API keys, access tokens, or other credentials to GitHub.

7. AUTHENTICATION

The auth/ directory contains the authentication and token-generation utilities:

- auth.py
- generate_tokens.py
- testing.py

Use these utilities according to the authentication flow configured for your Fyers API
application.

8. RUNNING THE PROJECT

Open a terminal in the HFT_SUBMISSION project root and run:

    python .\src\run_live.py

Make sure the required environment variables and Fyers API credentials are configured
before starting the application.

9. LOGGING AND REPORTS

The system records trading activity and session-level statistics.

Generated reports can include:
- Total trades
- Profitable trades
- Losing trades
- Win rate
- Net PnL

Trade activity is stored in CSV format and session-level results are summarized separately
for analysis.

10. RISK MANAGEMENT

The project includes several protections intended to control simulated trading activity:

- Trade cooldown protection
- Market regime filtering
- Stop Loss system
- Take Profit system
- Position state management
- Duplicate trade prevention

11. TECHNOLOGIES USED

- Python
- Fyers API v3
- WebSocket Streaming
- Pandas
- NumPy
- Colorama

12. PAPER TRADING DISCLAIMER

This project is a simulation system developed for educational, research, and internship
evaluation purposes.

It currently performs paper trading simulation only and does not place real market orders.
Live trading would require additional testing, validation, monitoring, risk controls, and
compliance with applicable financial regulations.
