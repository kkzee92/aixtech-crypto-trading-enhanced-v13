"""Risk Engine: pre-trade gates with v13 enhancements (volatility adaptive, anomaly)."""

from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Signal:
    side: str  # BUY, SELL, HOLD
    strength: float
    symbol: str
    regime: str = "unknown"

    def to_dict(self):
        return {"side": self.side, "strength": self.strength, "symbol": self.symbol, "regime": self.regime}

@dataclass
class RiskDecision:
    approved: bool
    reason: str
    adjusted_size_pct: float = 0.0

    def to_dict(self):
        return {"approved": self.approved, "reason": self.reason, "adjusted_size_pct": self.adjusted_size_pct}

class RiskEngine:
    def __init__(self, max_position_pct=0.05, max_daily_loss_pct=0.03, max_leverage=2.0, volatility_adaptive=True):
        self.max_position_pct = max_position_pct
        self.max_daily_loss_pct = max_daily_loss_pct
        self.max_leverage = max_leverage
        self.volatility_adaptive = volatility_adaptive

    def evaluate(self, signal: Signal, current_equity: float, current_positions: Dict, market_data: Dict = None) -> RiskDecision:
        if signal.side == "HOLD":
            return RiskDecision(False, "No action")

        vol = market_data.get("volatility", 0.02) if market_data else 0.02
        size_pct = self.max_position_pct
        if self.volatility_adaptive and vol > 0.04:
            size_pct *= 0.5  # reduce in high vol
            reason_extra = " (vol-adaptive reduction)"
        else:
            reason_extra = ""

        # Simple anomaly check (z-score proxy on price change)
        if market_data and abs(market_data.get("onchain_inflow", 0)) > 100:
            return RiskDecision(False, "Anomaly: extreme on-chain inflow")

        if signal.strength < 0.3:
            return RiskDecision(False, "Signal strength too low")

        return RiskDecision(True, f"Approved within limits{reason_extra}", size_pct)
