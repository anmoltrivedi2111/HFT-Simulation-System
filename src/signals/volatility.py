#Detects market instability using price volatility

from signals.base_signal import BaseSignal
from utils.config import config

class VolatilitySignal(BaseSignal):
    def __init__(self):
        super().__init__("volatility")
        
    def compute(self, state: dict) -> dict:
        #uses standard deviation to detect volatlity
        volatility = state.get("volatility",0)
        
        threshold = config.SIGNAL["VOLATILITY_THRESHOLD"]
        
        #high_volatility -> unstable market
        if volatility > threshold:
            return self.format_output(-1, volatility, "High Volatility (Risk)")

        #very low volatility -> no movement
        elif volatility ==0:
            return self.format_output(0, volatility, "No Movement")
        
        else:
            return self.format_output(1, volatility, "Normal Volatility")
        
        