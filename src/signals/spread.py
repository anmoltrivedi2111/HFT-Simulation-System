#Measures bid-ask spread quality

from signals.base_signal import BaseSignal

class SpreadSignal(BaseSignal):
    
    def __init__(self):
        super().__init__("spread")
        
    def compute(self, state: dict) -> dict:
        
        #uses bid-ask spread to evaluate liquidity quality
        
        bid = state.get("bid", 0)
        ask = state.get("ask", 0)
        
        #invalid market data
        if bid == 0 or ask == 0:
            return self.format_output(
                0,
                0.0,
                "Insufficient bid/ask data"
            )
        spread = ask - bid
        
        #simple thresholds
        
        tight_threshold = 0.05
        wide_threshold = 0.20
        
        #tight spread -> efficient market
        if spread < tight_threshold:
            return self.format_output(1,spread, "Tight spread (good liquidity)")
        #wide spread -> dangerous execution
        elif spread > wide_threshold:
            return self.format_output(-1, spread, "Wide spread (poor liquidity)")
        
        else:
            return self.format_output(0, spread, "Normal spread")
        
        