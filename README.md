# ⚡ High Frequency Trading (HFT) Simulation System

### Real-time, event-driven paper trading engine built with Python & Fyers WebSocket

> **⚠️ Educational / Research Project**
>
> This system is designed for educational, research, and internship evaluation purposes.
> It performs **paper trading simulation only** and does **not place real market orders**.
> It should not be used directly for live financial trading without further testing,
> validation, risk controls, and regulatory compliance.

---

## 📌 Overview

This project is a **real-time High Frequency Trading (HFT) simulation system** developed using
**Python** and **Fyers API WebSocket market data**.

The system continuously receives live market ticks, processes market-microstructure signals,
evaluates market conditions, applies risk management, and generates simulated trading
decisions in real time.

The architecture follows an **event-driven trading workflow** similar to a basic algorithmic
trading engine.

---

## 🔄 System Workflow

```text
┌──────────────────────┐
│  Live Market Data    │
│  Fyers WebSocket     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Tick Processing    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Signal Generation   │
│  11 Microstructure   │
│      Signals         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Score Evaluation   │
│  Weighted Signals    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Risk Validation    │
│ Regime + Risk Rules  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Decision Engine    │
│   Buy / Sell / Hold  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Paper Trade Execution│
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Logging & Analytics │
└──────────────────────┘
```

---

## 🚀 Key Features

| Area | Capabilities |
|---|---|
| 📡 Market Data | Real-time Fyers WebSocket streaming |
| 📊 Monitoring | Multi-symbol live market monitoring |
| ⚙️ Architecture | Event-driven trading pipeline |
| 🧠 Signals | Multiple market-microstructure signals |
| 🎯 Decision Making | Weighted scoring + Buy/Sell confirmation |
| 🛡️ Risk | Regime filtering, cooldown, SL/TP |
| 💼 Execution | Paper trading execution |
| 📈 Analytics | Realized PnL & trade statistics |
| 📝 Logging | CSV trade logs & session summaries |
| 🖥️ Monitoring | Colorized terminal output |
| 🐞 Debugging | Detailed signal-analysis/debug mode |

---

## 🧠 Trading Signals

The system uses the following market-microstructure signals:

| # | Signal |
|---:|---|
| 1 | Order Imbalance |
| 2 | Microprice |
| 3 | Order Flow |
| 4 | Volatility Detection |
| 5 | Burst Detection |
| 6 | Slippage Detection |
| 7 | Liquidity Consumption |
| 8 | Absorption Detection |
| 9 | Trade Intensity |
| 10 | Average Trade Size |
| 11 | Spread Analysis |

---

## 🛡️ Risk Management

The simulation includes multiple protections designed to control trading activity:

- **Trade cooldown protection**
- **Market regime filtering**
- **Stop Loss system**
- **Take Profit system**
- **Position state management**
- **Duplicate trade prevention**

---

## 📁 Project Structure

```text
HFT_SUBMISSION/
│
├── auth/
│   ├── auth.py
│   ├── generate_tokens.py
│   └── testing.py
│
├── src/
│   ├── core/
│   │   ├── decision_engine.py
│   │   ├── pipeline.py
│   │   ├── score_engine.py
│   │   └── state_manager.py
│   │
│   ├── data/
│   │   ├── data_adapter.py
│   │   └── tick_classifier.py
│   │
│   ├── execution/
│   │   └── order_router.py
│   │
│   ├── live/
│   │   └── fyers_stream.py
│   │
│   ├── risk/
│   │   ├── regime_detector.py
│   │   └── risk_manager.py
│   │
│   ├── signals/
│   │   ├── absorption.py
│   │   ├── avg_trade_size.py
│   │   ├── base_signal.py
│   │   ├── burst_detection.py
│   │   ├── liquidity_consumption.py
│   │   ├── microprice.py
│   │   ├── order_flow.py
│   │   ├── order_imbalance.py
│   │   ├── slippage.py
│   │   ├── spread.py
│   │   ├── trade_intensity.py
│   │   └── volatility.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   └── run_live.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

> Runtime-generated files under `logs/` are excluded from version control.

---

## 🧩 Module Responsibilities

### `src/core/`
Core decision-making and pipeline components.

- `pipeline.py` — central processing pipeline
- `score_engine.py` — signal score evaluation
- `decision_engine.py` — trading decision handling
- `state_manager.py` — position/state management

### `src/data/`
Market-data processing and classification.

- `data_adapter.py`
- `tick_classifier.py`

### `src/signals/`
Individual market-microstructure signal implementations.

Each signal is separated into its own module to keep the signal layer modular and easier to
extend.

### `src/risk/`
Risk and market-regime handling.

- `regime_detector.py`
- `risk_manager.py`

### `src/execution/`
Paper-trade order routing.

- `order_router.py`

### `src/live/`
Live market-data streaming.

- `fyers_stream.py`

### `src/utils/`
Shared configuration and logging utilities.

- `config.py`
- `logger.py`

### `auth/`
Authentication and token-generation utilities for the Fyers API.

---

## 🛠️ Technologies

- **Python**
- **Fyers API v3**
- **WebSocket Streaming**
- **Pandas**
- **NumPy**
- **Colorama**

---

## ⚙️ Setup

### 1. Install dependencies

From the project root:

```bash
pip install -r requirements.txt
```

### 2. Configure API credentials

Use `.env.example` as the template for the required environment variables.

Create a local `.env` file and configure it with **your own Fyers API credentials**.

```text
.env.example  →  .env
```

> 🔐 **Never commit real API keys, access tokens, or other credentials to GitHub.**
> The `.gitignore` included in this project excludes `.env`.

---

## ▶️ Running the Project

From the project root directory:

### Windows

```bash
python .\src\run_live.py
```

Make sure the required environment variables and Fyers API credentials are configured
before starting the application.

---

## 📊 Logging & Reports

During execution, the system can generate trading logs and session-level reports containing
information such as:

- Total trades
- Profitable trades
- Losing trades
- Win rate
- Net PnL

Generated runtime logs are intentionally excluded from this repository.

---

## 📌 Current Scope

This project currently focuses on **real-time paper trading simulation**.

It does **not** place real market orders.

The system is intended to demonstrate an event-driven trading architecture involving:

**Market Data → Tick Processing → Signal Generation → Scoring → Risk Validation → Decision
Making → Paper Execution → Analytics**

---

## ⚠️ Disclaimer

This project is developed for **educational, research, and internship evaluation purposes**.

It is not financial advice and is not a production-ready live trading system. Live deployment
would require significantly more testing, validation, monitoring, reliability engineering,
risk controls, and compliance with applicable financial regulations.

---

### 👨‍💻 Developed by Anmol Trivedi
