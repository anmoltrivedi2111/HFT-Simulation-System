#combines all signal outputs into weighted score

from utils.config import config

class ScoreEngine:
    def __init__(self):
        #signal importance weights
        self.weights = config.SIGNAL["WEIGHTS"]
        
    def calculate(self, signal_results:dict) -> dict:
        #combines weighted signal outputs into final score
        total_score = 0.0
        
        #stores per-signal contribution
        breakdown = {}
        
        for signal_name, result in signal_results.items():
            
            signal = result["signal"]
            
            #default weight if missing
            weight = self.weights.get(signal_name, 1.0)
            
            weighted_score = signal * weight
            
            total_score+= weighted_score
            total_score = round(total_score, 2)
            breakdown[signal_name] = {
                "signal":signal,
                "weight":weight,
                "weighted_score":weighted_score
            }
            
            abs_score = round(total_score, 2)
            
            #confidence estimation
            if abs_score >=4:
                confidence = "HIGH"
            elif abs_score >= 2:
                confidence = "MEDIUM"
                
            else:
                confidence="LOW"
                
        return {
            "score":total_score,
            "confidence":confidence,
            "breakdown":breakdown
        }
        