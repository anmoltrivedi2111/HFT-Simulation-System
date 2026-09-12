#Detects Sudden spikes in activity and assign direction.

from signals.base_signal import BaseSignal
from utils.config import config

class BurstDetectionSignal(BaseSignal):
    def __init__(self):
        super().__init__("burst_detection")
    
    def compute(self, state: dict) -> dict:
        
        #Detects burst using TPS and aligns with flow direction
        
        tps = state.get("tps",0)
        net_flow = state.get("net_flow",0)
        
        threshold = config.SIGNAL["BURST_THRESHOLD"]
        
        #no burst -> ignore
        
        if tps <= threshold:
            return self.format_output(0,tps,"No Burst")

        #burst + direction
        if net_flow > 0:
            return self.format_output(1, tps, "Buy Burst Detected")
        elif net_flow < 0:
            return self.format_output(-1, tps, "Sell Burst Detected")
        else:
            return self.format_output(0, tps, "Burst with No Direction")
        
        