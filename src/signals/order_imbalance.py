#Detects buy/sell dominance using net flow.

from signals.base_signal import BaseSignal
from utils.config import config

class OrderImbalanceSignal(BaseSignal):
    def __init__(self):
        super().__init__("order imbalance")
    
    def compute(self, state: dict) -> dict:
        #Using net flow to detect Imbalance
        net_flow = state.get("net_flow",0)
        
        #normalize flow
        total = abs(net_flow)+ 1 if net_flow!= 0 else 1
        imbalance = net_flow/total
        
        threshold = config.SIGNAL["IMBALANCE_THRESHOLD"]
        
        #decide signal
        if imbalance > threshold:
            return self.format_output(1, imbalance, "Strong buy Imbalance")
        
        elif imbalance < -threshold:
            return self.format_output(-1, imbalance, "Strong sell Imbalance")
        else:
            return self.format_output(0, imbalance, "No Strong Imbalance")