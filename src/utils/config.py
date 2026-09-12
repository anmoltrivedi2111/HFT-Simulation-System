from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    
    def __init__(self):
        
        #API config
        self.API = {
            "CLIENT_ID": os.getenv("CLIENT_ID"),
            "ACCESS_TOKENS": os.getenv("ACCESS_TOKENS"),
            
            #STOCKS_LIST
            "SYMBOLS":[
                "NSE:PNB-EQ",
                "NSE:CANBK-EQ",
                "NSE:SAIL-EQ",
                "NSE:IDFCFIRSTB-EQ",
                "NSE:SBIN-EQ",
                "NSE:BANKBARODA-EQ"
            ]
        }
        
        #DATA SETTINGS
        self.DATA = {
            "MAX_TICKS":500,
            "MAX_TRADES":200,
            "TIME_WINDOW":5 # 5 seconds
        }
        
        #SIGNAL SETTINGS
        self.SIGNAL = {
            "IMBALANCE_THRESHOLD":0.6,
            "VOLATILITY_THRESHOLD":0.002,
            "BURST_THRESHOLD":1.5,
            "SLIPPAGE_THRESHOLD":0.002,
            
            "WEIGHTS":{
                'order_imbalance':1.2,
                'microprice':1.0,
                'order_flow':1.2,
                'volatility':0.8,
                'burst_detection':1.1,
                'slippage':0.5,
                'spread':0.5,
                'liquidity_consumption':1.0,
                'absorption':1.0,
                'trade_intensity':0.8,
                'Avg_trade_size':0.4
            }
        }
        
        #RISK_SETTINGS
        self.RISK = {
            "MAX_POSITION":1,
            "MAX_LOSS_PER_TRADE":0.01,
            "MAX_DAILY_LOSS":0.03,
            "LOW_LIQUIDITY":50,
            "HIGH_VOLATILITY": 0.02,
            "TRADE_COOLDOWN": 10,
            "STOP_LOSS": 0.01,
            "TAKE_PROFIT": 0.02,

        }
        
        #EXECUTION SETTINGS
        self.EXECUTION = {
            "ORDER_TYPE":"MARKET",
            "QUANTITY":1,
            "PRICE_BUFFER":0.0005
        }
        
        #MODE_SETTINGS
        
        self.MODE = {
            "PAPER_TRADING":True,
            "DEBUG":False
        }
        
#global config instance
config = Config()