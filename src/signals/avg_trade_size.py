#detects usually large average size trades

from signals.base_signal import BaseSignal

class AvgTradeSizeSignal(BaseSignal):
    
    def __init__(self):
        super().__init__("Avg_trade_size")
        
    def compute(self, state:dict) -> dict:
        
        #uses average trade volume to detect large participation
        
        trades = state.get("trades",[])
        
        if not trades:
            return self.format_output(0,0.0, "No trade data")
        
        volumes = [
            trade.get("volume",0)
            for trade in trades
        ]
        
        avg_size = sum(volumes) / len(volumes)
        
        #simple thresholds
        high_threshold = 1000
        low_threshold = 100
        
        if avg_size > high_threshold:
            return self.format_output(1,avg_size, "Large average trade size")
        
        elif avg_size < low_threshold:
            return self.format_output(-1, avg_size, "Small average trade size")
        
        else:
            return self.format_output(0, avg_size, "Normal average trade size")
        