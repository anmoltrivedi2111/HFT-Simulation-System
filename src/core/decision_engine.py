# Maintains stable BUY/SELL/HOLD decisions using signal confidence
import time
from utils.config import config


class DecisionEngine:
    def __init__(self):

        # prevents instant buy/sell flipping
        self.buy_streak = 0
        self.sell_streak = 0

        self.current_bias = "HOLD"
        self.current_position = {}

        # required stable confirmations
        self.confirmation_ticks = 2

        # last trade timestamps
        self.last_trade_time = {}
        self.entry_prices = {}
        
        #pnl tracking
        self.total_pnl = 0
        self.total_trades = 0
        self.wins = 0
        self.losses = 0
        
    def update_pnl(self, pnl):
        self.total_pnl+=pnl
        self.total_trades+=1
        
        if pnl > 0:
            self.wins+=1
        else:
            self.losses+=1
        
    def save_summary(self):
        if self.total_trades > 0:
            
            win_rate = (
                self.wins / self.total_trades
            ) * 100
        else:
            win_rate = 0
        
        with open('logs/session_summary.txt','w') as file:
            file.write(
            "========== SESSION SUMMARY ==========\n\n"
            )
            file.write(
                f"Total Trades: "
                f"{self.total_trades}\n"
            )

            file.write(
                f"Profitable Trades: "
                f"{self.wins}\n"
            )

            file.write(
                f"Losing Trades: "
                f"{self.losses}\n"
            )

            file.write(
                f"Profit Rate: "
                f"{win_rate:.2f}%\n"
            )

            file.write(
                f"Net PnL: "
                f"{self.total_pnl:.2f}\n"
            )
        
        
    def evaluate(
        self, signal_results: dict, risk_results: dict, symbol, current_price,score
    ) -> dict:
        
        # STOPLOSS / TAKE PROFIT
        position = self.current_position.get(symbol)
        entry_price = self.entry_prices.get(symbol)

        if position and entry_price:
            stop_loss = config.RISK["STOP_LOSS"]
            take_profit = config.RISK["TAKE_PROFIT"]

            # BUY POSITION

            if position == "BUY":
                pnl_pct = (current_price - entry_price) / entry_price

                # stop loss
                if pnl_pct <= -stop_loss:
                    
                    pnl = current_price - entry_price
                    self.update_pnl(pnl)
                    
                    self.current_position[symbol] = None

                    return {"action": "SELL", 
                            "reason": "Stop Loss Triggered"}
                    
                # take profit
                elif pnl_pct >= take_profit:
                    
                    pnl = current_price - entry_price
                    self.update_pnl(pnl)
                    
                    self.current_position[symbol] = None
                    
                    return {"action": "SELL",
                            "reason": "Take Profit Reached"}
            # SELL POSITION
            elif position == "SELL":

                pnl_pct = (entry_price - current_price) / entry_price
                # stoploss
                if pnl_pct <= -stop_loss:
                    self.current_position[symbol] = None
                    pnl = entry_price - current_price
                    self.update_pnl(pnl)
                    
                    return {
                        'action':'BUY',
                        'reason':'Stop Loss Triggered'
                        
                    }
                #take profit
                elif pnl_pct >= take_profit:
                    pnl = entry_price - current_price
                    self.update_pnl(pnl)
                    
                    self.current_position[symbol] = None
                    
                    return {
                        'action':'BUY',
                        'reason':'Take Profit Reached'
                    }
                    
        # adding cooldown period
        cooldown = config.RISK["TRADE_COOLDOWN"]
        current_time = time.time()

        last_trade = self.last_trade_time.get(symbol)

        if last_trade:
            elapsed = current_time - last_trade

            if elapsed < cooldown:

                remaining = round(cooldown - elapsed, 2)

                return {
                    "action": "HOLD",
                    "reason": f"Cooldown active ({remaining}s remaining)",
                }
        current_position = self.current_position.get(symbol)

        
                # Revalidates market direction on every tick

        # risk manager blocked trading
        if not risk_results["allowed"]:
            self.current_bias = "HOLD"

            return {"action": "HOLD", "reason": risk_results["reason"]}
        buy_conditions = 0
        sell_conditions = 0

        # count signal directions
        # directional trading signals only.
        strong_signals = [
            "order_imbalance",
            "order_flow",
            "liquidity_consumption",
            "burst_detection",
        ]

        # supportive directional signals
        supportive_signals = ["microprice", "absorption", "trade_intensity"]

        # count weighted confirmations
        for name, result in signal_results.items():
            signal = result["signal"]

            # buy side
            if signal == 1:
                # strong confirmation
                if name in strong_signals:
                    buy_conditions += 2
                # supportive confirmations
                elif name in supportive_signals:
                    buy_conditions += 1

            # Sell side
            elif signal == -1:
                # strong confirmation
                if name in strong_signals:
                    sell_conditions += 2
                # supportive confirmations
                elif name in supportive_signals:
                    sell_conditions += 1

        # Buy Confirmation logic

        if buy_conditions >= 6 or score >=6:

            self.buy_streak += 1
            self.sell_streak = 0

            # require stable confirmation
            if self.buy_streak >= self.confirmation_ticks:
                # avoid duplicates buy entries
                if current_position == "BUY":

                    return {"action": "HOLD", "reason": "Already in BUY position"}

                self.current_position[symbol] = "BUY"
                self.entry_prices[symbol] = current_price
                self.current_bias = "BUY"
                self.last_trade_time[symbol] = time.time()

                return {
                    "action": "BUY",
                    "reason": f"{buy_conditions} BUY conditions satisfied",
                }
            # still waiting for confirmation
            return {"action": "HOLD", "reason": "Waiting for Buy confirmation"}

        # Sell confirmation logic

        elif sell_conditions >= 4 or score <= -4:
            self.sell_streak += 1
            self.buy_streak = 0

            # requires stable confirmation
            if self.sell_streak >= self.confirmation_ticks:

                if current_position == "SELL":

                    return {"action": "HOLD", "reason": "Already in sell position"}
                self.current_position[symbol] = "SELL"
                self.entry_prices[symbol] = current_price
                self.current_bias = "SELL"
                self.last_trade_time[symbol] = time.time()

                return {
                    "action": "SELL",
                    "reason": f"{sell_conditions} SELL conditions satisfied",
                }

            return {"action": "HOLD", "reason": "Waiting for SELL confirmation"}
        # reset symbol positions
        if buy_conditions < 6 and sell_conditions < 4:
            self.current_position[symbol] = None

        # insufficient confirmations
        self.buy_streak = 0
        self.sell_streak = 0

        self.current_bias = "HOLD"

        self.save_summary()
        return {"action": "HOLD", "reason": "Conditions not stable"}
