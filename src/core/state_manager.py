from collections import deque
import statistics
import time
from utils.config import config

class StateManager:
    
    def __init__(self):
        #Initializing state dictionary for all symbols,
        self.state = {}
        
        for symbol in config.API["SYMBOLS"]:
            self.state[symbol] = {
                "prices":deque(maxlen=config.DATA["MAX_TICKS"]),
                "trades": deque(maxlen=config.DATA["MAX_TRADES"]),
            }
    
    def update(self,tick: dict):
        symbol = tick["symbol"]
        
        if symbol not in self.state:
            return
        
        symbol_state = self.state[symbol]
        
        #Storing prices
        symbol_state["prices"].append(tick["price"])
        
        #Storing trade (side + timestamp)
        symbol_state["trades"].append({
            "side": tick.get("side", "NEUTRAL"),
            "timestamp": tick["timestamp"],
            "volume": tick.get("volume", 0)
        })
    
    
    def compute_metrics(self,symbol: str) -> dict:
        
        #computing key matrices for a symbol
        symbol_state = self.state.get(symbol)
        
        if not symbol_state:
            return {}
        
        prices = list(symbol_state["prices"])
        trades = list(symbol_state["trades"])
        
        #NET FLOW (BUY - SELL)
        
        buy_count = sum(1 for t in trades if t["side"] == "BUY")
        sell_count = sum(1 for t in trades if t["side"] == "SELL")
        
        net_flow = buy_count - sell_count
        
            
        #TRADES PER SECOND
        current_time = time.time()
        window = config.DATA["TIME_WINDOW"]
        
        recent_trades = [
            t for t in trades
            if current_time - t["timestamp"] <= window
        ]
        
        tps = len(recent_trades) / window if window > 0 else 0
        
        #VOLATILITY (std_deviation)
        
        returns = []
        
        for i in range(1, len(prices)):
            
            prev_price = prices[i - 1]
            curr_price = prices[i]
            
            #avoid divide by 0
            if prev_price == 0:
                continue
            
            pct_returns = (
                (curr_price - prev_price)/ prev_price
                
            )
            
            returns.append(pct_returns)
            
            #need enough samples
        if len(returns) >= 2:
            volatility = statistics.stdev(returns)
                
        else:
            volatility = 0.0
            
        

        
        return {
            "net_flow":net_flow,
            "tps":tps,
            "volatility":volatility
            
        }
        
    