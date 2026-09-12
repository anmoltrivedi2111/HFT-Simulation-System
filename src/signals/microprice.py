#Detects Price pressure using bid/ask midpoint comparison

from signals.base_signal import BaseSignal

class MicroPriceSignal(BaseSignal):
    
    def __init__(self):
        super().__init__("microprice")
    
    def compute(self, state: dict) -> dict:
        
        #Compares current price with microprice
        
        price = state.get("price",0)
        bid = state.get("bid",0)
        ask = state.get("ask",0)
    
    #avoid invalid data
        if bid ==0 or ask ==0:
            return self.format_output(0,0.0, "Insufficient bid/ask data")
        
        microprice = (bid+ask) / 2
        
        diff = price - microprice
        
        if diff < 0:
            return self.format_output(1, diff, "Price below microprice (buy pressure)")
        
        elif diff > 0:
            return self.format_output(-1, diff, "Price above microprice (sell pressure)")
        
        else:
            return self.format_output(0, diff, "Price equals microprice")
        