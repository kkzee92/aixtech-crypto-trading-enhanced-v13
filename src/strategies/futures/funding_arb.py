"""Futures funding rate arbitrage strategy (delta-neutral conceptual)."""

from src.risk.risk_engine import Signal

class FundingArbStrategy:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def generate_signal(self, market_data: dict) -> Signal:
        funding = market_data.get("funding_rate", 0)
        strength = min(abs(funding) * 10000, 1.0)  # scale
        side = "BUY" if funding > 0.00005 else ("SELL" if funding < -0.00005 else "HOLD")
        # In real arb: opposite on perp, but signal here is directional for demo
        regime = "funding_positive" if funding > 0 else "funding_negative"
        return Signal(side=side, strength=strength, symbol=self.symbol, regime=regime)
