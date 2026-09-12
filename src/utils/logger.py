import csv
import os
from datetime import datetime
class TradeLogger:
    
    def __init__(self):
        session_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        self.log_dir = "logs"
        #create logs folder
        os.makedirs(self.log_dir, exist_ok=True)
        
        self.log_file = os.path.join(
            self.log_dir,
            f"{session_time}.csv"
        )
        
        
        #creating csv with headers
        if not os.path.exists(self.log_file):
        
        
            with open(self.log_file, "w", newline="" ) as file:
                
                writer = csv.writer(file)
                
                writer.writerow([
                    'timestamp',
                    'symbol',
                    'action',
                    'score',
                    'confidence',
                    'reason'
                ])
                
    def log_trade(self, symbol, action, score, confidence, reason, timestamp,):
        with open (self.log_file, "a", newline="") as file:
            writer = csv.writer(file)
            formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([
            formatted_time,
            symbol,
            action,
            score,
            confidence,
            reason    
            ])
            
            