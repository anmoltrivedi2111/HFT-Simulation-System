#Final safety layer before trade decisions

class RiskManager:
    def __init__(self):
        pass
    
    def evaluate(
        self,score_result:dict,regime_result:dict,)->dict:
        #Evaluates whether trading is allowed
        
        confidence = score_result.get("confidence","LOW")
        regime = regime_result.get("regime","UNKNOWN")
        safe = regime_result.get("safe",False)
        
        #unsafe makret -> block trading
        
        if not safe:
            return {
                "allowed":False,
                "reason":f"Unsafe market regime {regime}"
            }
            
        #low confidence -> avoid weak trades
        if confidence =="LOW":
            return {
                'allowed':False,
                'reason':'Low confidence score'
            }
            
        #trading allowed
        return {
            'allowed':True,
            'reason':'Conditions acceptable'
        }
        
        