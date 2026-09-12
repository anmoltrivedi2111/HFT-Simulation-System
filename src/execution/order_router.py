#Simulating paper trade execution
from datetime import datetime

class OrderRouter:
    def __init__(self):
        #stores paper trade history
        
        self.trade_history = []
        
    def place_order(self, symbol:str, action:str, price:float) -> None:
        #Simulates paper trade execution
        
        #HOLD means no action
        if action == "HOLD":
            return 
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        trade = {
            'symbol':symbol,
            'action':action,
            'price':price,
            'timestamp':timestamp
        }
        
        #Store trade for later analysis
        self.trade_history.append(trade)
        
        print(
            f"[PAPER TRADE] "
            f"{symbol} |"
            f"{action} |"
            f"{price} |"
            f"{timestamp}"
            
        )
        
    def get_trade_history(self) -> list:
        #Returns all simulated trades
        
        return self.trade_history
    