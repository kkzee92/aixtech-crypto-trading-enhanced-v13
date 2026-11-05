"""Spot multi-factor momentum strategy with regime awareness (v13)."""

from src.risk.risk_engine import Signal

class SpotMomentumStrategy:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def generate_signal(self, market_data: dict) -> Signal:
        price = market_data.get("price", 0)
        vol = market_data.get("volume", 0)
        inflow = market_data.get("onchain_inflow", 0)
        volatility = market_data.get("volatility", 0.02)

        # Multi-factor: price trend proxy + volume + on-chain
        trend_score = 1 if price > 65000 else 0.5
        volume_score = min(vol / 1000, 1.0)
        onchain_score = 1 if inflow > 0 else 0.4
        strength = (trend_score + volume_score + onchain_score) / 3

        # Regime: high vol = caution, else trending if strength high
        regime = "high_vol" if volatility > 0.03 else ("trending" if strength > 0.6 else "ranging")

        side = "BUY" if strength > 0.55 else "HOLD"
        return Signal(side=side, strength=strength, symbol=self.symbol, regime=regime)
