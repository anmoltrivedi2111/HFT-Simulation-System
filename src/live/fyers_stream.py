#websocket integration

import os
from dotenv import load_dotenv

from fyers_apiv3.FyersWebsocket import data_ws

from core.pipeline import Pipeline
from utils.config import config

#loading environment
load_dotenv()

DEBUG_MODE = False
pipeline = Pipeline()

class FyersLiveFeed:
    def __init__(self):
        self.access_tokens = os.getenv("ACCESS_TOKENS")
        
        self.symbols = config.API["SYMBOLS"]
        
        self.fyers = data_ws.FyersDataSocket(
            access_token=self.access_tokens,
            log_path="",
            litemode=False,
            write_to_file=False,
            reconnect=True,
            on_connect=self.on_open,
            on_close=self.on_close,
            on_error=self.on_error,
            on_message=self.on_message
        )
        
    #websocket connected
    def on_open(self):
        
        print("\n[FYERS] Websocket Connected")
        
        print("\nSubscribing Symbols:")
        
        for symbol in self.symbols:
            print(symbol)
            
        self.fyers.subscribe(
            symbols = self.symbols,
            data_type="SymbolUpdate"
        )
        self.fyers.keep_running()
        
    #live market ticks
    def on_message(self,message):
        
        try:
            #temporary debug
            if DEBUG_MODE:
                print("\n RAW FYERS MESSAGE: ")
                print(message)
                
            tick = {
                
                'symbol':message.get('symbol'),
                'ltp':message.get('ltp',0),
                'bid_price': message.get('bid_price',0),
                'ask_price':message.get('ask_price', 0),
                'bid_size': message.get('bid_size', 0),
                'ask_size': message.get('ask_size', 0),
                'volume': message.get('vol_traded_today', 0),
                'timestamp':message.get('exch_feed_time', 0),
                
            }
            pipeline.process_ticks(tick)
            
        except Exception as e:
            
            print("\n [PIPELINE ERROR]")
            print(e)
            
    
    #websocket closed
    def on_close(self,message):
        
        print("\n[FYERS] Connection Closed")
            
        print(message)
        
    #websocket error
    def on_error(self, message):
        
        print("\n [FYERS ERROR] ")
        
        print(message)
    #start websocket
    def start(self):
        
        print("\n Start Fyers Websocket...")
        
        self.fyers.connect()
        