# Detects aggressive price movement (liquidity taking)

from signals.base_signal import BaseSignal

class LiquidityConsumptionSignal(BaseSignal):
    
    def __init__(self):
        super().__init__("liquidity consumption")
        
    def compute(self, state: dict) -> dict:
        #Uses recent price movement to detect aggressive activity
        
        prices = state.get("prices", [])
        
        #need atleast two prices
        if len(prices) < 2:
            return self.format_output(0,0.0, "Not enough Data")
        
        #last two prices
        last_price = prices[-1]
        prev_price = prices[-2]
        
        change = last_price-prev_price
        
        #small threshold to ignore noise
        threshold= 0.05 
        
        if change > threshold:
            return self.format_output(1, change, "Aggressive buying (liquidity consumed)")
        
        elif change < -threshold:
            return self.format_output(-1, change, "Aggressive selling (liquidity consumed)")
        
        else:
            return self.format_output(0, change, "No significant consumption")

