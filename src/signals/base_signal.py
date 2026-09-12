#This module defines a standard interface for all signals

class BaseSignal:
    #Base class for all signals and every signal inherits from it.
    def __init__(self, name: str):
        self.name = name
        
    
    def compute(self, state: dict) -> dict:
        #This method must be implemented by all child classes.
        
        raise NotImplementedError(f"{self.name} must implement compute()")
    
    def format_output(self, signal: int, value: float, reason: str) -> dict:
        
        #This function standardizes output format across all signals. 
        
        if signal not in (-1, 0, 1):
            raise ValueError("Signal must be -1, 0, or 1")
        
        return {
            "signal": signal,
            "value":float(value),
            "reason":reason
        }