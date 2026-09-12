class TickClassifier:
    
    def __init__(self):
        pass
    
    def classify(self,tick:dict)-> dict:
        
        price = tick["price"]
        bid= tick["bid"]
        ask= tick["ask"]
        
        #DEFAULT ASSUMPTION
        side = "NEUTRAL"
        
        #AGGRESSIVE BUYER (LIFTING ASK)
        if ask > 0 and price >= ask:
            side = "BUY"
        
        #AGGRESSIVE SELLING (hitting the bid)
        elif bid > 0 and price <= bid:
            side = "SELL"
        
        #attach classification
        new_tick = tick.copy()
        new_tick["side"] = side
        
        
        return new_tick
    