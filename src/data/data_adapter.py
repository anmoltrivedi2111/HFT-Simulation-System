import time

class DataAdapter:
    
    def __init__(self):
        pass
    
    def adapt(self,raw_tick: dict) ->dict:
        
        symbol = raw_tick.get("symbol")
        
        #LAST_TRADED_PRICE
        price = raw_tick.get("ltp")
        if price is None:
            price = raw_tick.get("price")
        
        #CRITICAL DATA MISSING --> SKIP EARLY
        if symbol is None or price is None:
            return None
        
        #ORDER_BOOK VALUES (may not always present)
        bid = raw_tick.get("bid_price",0.0) or raw_tick.get("bid", 0)
        ask = raw_tick.get("ask_price",0.0) or raw_tick.get("ask", 0)
        
        #volume (fallback to 0 if missing)
        volume = raw_tick.get("volume",0)
        
        #timestamp  (using system time if not provided)
        timestamp= raw_tick.get("timestamp",time.time())
        
        #IF CRITICAL DATA MISSING--> SKIP TICK
        
        return {
            "symbol":symbol,
            "price":float(price),
            
            "bid":float(bid),
            "ask":float(ask),
            
            "volume":float(volume),
            "timestamp":float(timestamp),
            
            "bid_size":raw_tick.get("bid_size", 0),
            "ask_size":raw_tick.get("ask_size", 0)
            
        }
        