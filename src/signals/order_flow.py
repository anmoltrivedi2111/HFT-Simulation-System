#Combines net flow and trade speed (tps) to detect strong pressure

from signals.base_signal import BaseSignal
from utils.config import config

class OrderFlowSignal(BaseSignal):
    def __init__(self):
        super().__init__("order_flow")
        
    def compute(self, state: dict) -> dict:
        #uses net flow + tps to detect momentum
        
        net_flow = state.get("net_flow",0)
        tps = state.get("tps",0)
        
        #avoid noise: ignore low activity
        if tps < 0.2:
            return self.format_output(0, tps, "Low trading activity")
        
        #combine direction + speed
        flow_strength = net_flow * tps
        
        if flow_strength > 0:
            return self.format_output(1, flow_strength, "Buy flow with activity")
        
        elif flow_strength < 0:
            return self.format_output(-1, flow_strength, "Sell flow with activity")
        
        else:
            return self.format_output(0, flow_strength, "No clear flow")