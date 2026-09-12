#Detects when market absorbs pressure without price movement

from signals.base_signal import BaseSignal

class AbsorptionSignal(BaseSignal):
    
    def __init__(self):
        super().__init__("absorption")
    
    def compute(self, state: dict) -> dict:
        
        #detects absorption using flow vs price movement
        
        net_flow = state.get("net_flow",0)
        prices = state.get("prices",[])
        
        #need at least two prices
        if len(prices) < 2:
            return self.format_output(0,0.0, "Not enough data")
        
        last_price = prices[-1]
        prev_price = prices[-2]
        
        price_change = last_price - prev_price
        
        #threshold for "no movement"
        
        threshold = 0.02
        value = abs(net_flow)
        #BUY pressure but price not rising -> SELL absorption
        if net_flow > 0 and abs(price_change) < threshold:
            return self.format_output(-1, value, "Buy absorption (sellers strong)")
        
        #SELL pressure but price not falling -> BUY absorption
        elif net_flow < 0 and abs(price_change) < threshold:
            return self.format_output(1, value, "Sell absorption (buyers strong)")
        
        else:
            return self.format_output(0, abs(price_change), "No absorption")
        