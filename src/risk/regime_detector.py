#detects current market condition

from utils.config import config

class RegimeDetector:
    
    def __init__(self):
        pass
    
    def detect(self, state:dict) -> dict:
        
        #detects market regime using volatility and activity
        
        volatility= state.get("volatility",0)
        tps = state.get("tps",0)
        
        high_volatility = config.RISK.get("HIGH_VOLATILITY",0.003)
        
        #unstable market
        if volatility > high_volatility:
            return {
                "regime":"HIGH_VOLATILITY",
                "safe":False
                
            }
        #inactive market
        elif tps < 0.2:
            return {
                "regime":"LOW_ACTIVITY",
                "safe":False
            }
        #tradable conditions
        return {
            "regime":"NORMAL",
            "safe":True
        }
    