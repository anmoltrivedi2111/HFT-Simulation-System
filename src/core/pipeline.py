
from colorama import Fore, Style, init
#Central pipeline for connecting all system components
from data.data_adapter import DataAdapter
from data.tick_classifier import TickClassifier

from core.state_manager import StateManager
from core.score_engine import ScoreEngine
from core.decision_engine import DecisionEngine

from risk.regime_detector import RegimeDetector
from risk.risk_manager import RiskManager

#utils
from utils.logger import TradeLogger
from utils.config import config

from execution.order_router import OrderRouter

#signals
from signals.order_imbalance import OrderImbalanceSignal
from signals.microprice import MicroPriceSignal
from signals.order_flow import OrderFlowSignal
from signals.volatility import VolatilitySignal
from signals.burst_detection import BurstDetectionSignal
from signals.slippage import SlippageSignal
from signals.liquidity_consumption import LiquidityConsumptionSignal
from signals.absorption import AbsorptionSignal
from signals.trade_intensity import TradeIntensitySignal
from signals.avg_trade_size import AvgTradeSizeSignal
from signals.spread import SpreadSignal

init(autoreset=True)

class Pipeline:
    
    def __init__(self):
        
        #Core data processing
        self.adapter = DataAdapter()
        self.classifier = TickClassifier()
        
        #state + engines
        self.state_manager = StateManager()
        self.score_engine = ScoreEngine()
        self.decision_engine = DecisionEngine()
        
        #risk layer
        self.regime_detector = RegimeDetector()
        self.risk_manager = RiskManager()
        
        #paper execution
        self.router = OrderRouter()
        
        #Tradelogger initialisation
        self.logger = TradeLogger()
        
        
        #all signals
        self.signals = [
        OrderImbalanceSignal(),
        MicroPriceSignal(),
        OrderFlowSignal(),
        VolatilitySignal(),
        BurstDetectionSignal(),
        SlippageSignal(),
        LiquidityConsumptionSignal(),
        AbsorptionSignal(),
        TradeIntensitySignal(),
        AvgTradeSizeSignal(),
        SpreadSignal()
        ]
        
    def process_ticks(self, raw_tick:dict):
        
        #process one incoming market tick
        
        #1: adapt raw data
        tick = self.adapter.adapt(raw_tick)
        
        if not tick:
            return
        
        #2: Classify trade signal
        tick = self.classifier.classify(tick)
        
        #3: update symbol state
        self.state_manager.update(tick)
        
        symbol = tick['symbol']
        
        #current symbol state
        symbol_state = self.state_manager.state[symbol]
        
        # computed metrics
        metrics = self.state_manager.compute_metrics(symbol)
        
        #merging all data into one state object
        commbined_state = {
            **symbol_state,
            **metrics,
            **tick
        }
        
        #4: compute signals
        
        signal_results = {}
        
        
        
        for signal in self.signals:
            result = signal.compute(commbined_state)
            
            signal_results[signal.name] = result
            
        #5: score engine
        
        score_result = self.score_engine.calculate(signal_results)
        score = score_result['score']
        #6: regime detection
        
        
        regime_result = self.regime_detector.detect(metrics)
        
        #7: risk evaluation
        
        risk_result = self.risk_manager.evaluate(
            score_result,
            regime_result
        )
        
        #8: decision making
        
        decision = self.decision_engine.evaluate(
            signal_results,
            risk_result,
            symbol,
            tick["price"],
            score
        )
        
        #9: paper trade execution
        self.router.place_order(
            symbol=symbol,
            action=decision['action'],
            price=tick['price']
        )
        
        self.logger.log_trade(
            symbol=symbol,
            action=decision['action'],
            score=score_result['score'],
            confidence=score_result['confidence'],
            reason=decision['reason'],
            timestamp=tick['timestamp']
        )
        #Debugging output
        confidence = score_result['confidence']
        
        show_output = (
            decision['action'] != "HOLD"
            or "confirmation" in decision['reason']
            or config.MODE["DEBUG"]
        )
        
        if show_output:
            print("\n ==============================")
            print("SYMBOL: ",symbol)
            action = decision['action']
            
            if action == "BUY":
                color = Fore.GREEN
            elif action == "SELL":
                color = Fore.RED
            else:
                color = Fore.YELLOW
                
            print(color + f"DECISION: {decision}")
            
            
            print("SCORE: ", score_result["score"])
            
            
            if confidence == "HIGH":
                conf_color = Fore.CYAN
            elif confidence == "MEDIUM":
                conf_color = Fore.MAGENTA
            else:
                conf_color = Fore.WHITE
                
            print(conf_color + f"CONFIDENCE: {confidence}")
            
            
            if config.MODE['DEBUG']:
                print("\nSIGNALS:")
                for name, result in signal_results.items():

                    signal = result["signal"]

                    if signal == 1:
                        signal_color = Fore.GREEN

                    elif signal == -1:
                        signal_color = Fore.RED

                    else:
                        signal_color = Fore.WHITE

                    print(
                        signal_color +
                        f"{name}: "
                        f"{result['signal']} | "
                        f"{result['reason']}"
                    )
            print("==============================")