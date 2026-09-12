#Detects execution inefficiency using price deviation

from signals.base_signal import BaseSignal
from utils.config import config

class SlippageSignal(BaseSignal):
    def __init__(self):
        super().__init__("slippage")
        
    def compute(self, state: dict) -> dict:
        #Measures slippage using price vs midpoint
        
        price = state.get("price",0)
        bid = state.get("bid",0)
        ask = state.get("ask",0)
        
        #invalid data handling
        if bid ==0 or ask == 0:
            return self.format_output(0,0.0, "Insufficient Data")
        
        midpoint = (bid + ask) / 2
        
        slippage = abs(price - midpoint) / midpoint
        
        threshold = config.SIGNAL["SLIPPAGE_THRESHOLD"]
        
        if slippage > threshold:
            return self.format_output(-1, slippage, "High Slippage")
        
        elif slippage < threshold / 2:
            return self.format_output(1, slippage, "Low Slippage")
        else:
            return self.format_output(0, slippage, "Normal Slippage")
        
        