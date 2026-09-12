#Measures sustained trade activity using TPS
from signals.base_signal import BaseSignal

class TradeIntensitySignal(BaseSignal):
    
    def __init__(self):
        super().__init__("trade_intensity")
        
    def compute(self,state: dict) -> dict:
        
        #uses TPS to detect activity intensity:
        
        tps = state.get("tps",0)
        
        #thresholds
        high_threshold = 0.8
        low_threshold = 0.2
        
        if tps > high_threshold:
            return self.format_output(1,tps, "High trade intensity")
        
        elif tps < low_threshold:
            return self.format_output(-1, tps, "Low trade activity")

        else:
            return self.format_output(0, tps, "Moderate activity")
        