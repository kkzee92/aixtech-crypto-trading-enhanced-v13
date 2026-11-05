# Trading Strategies by Asset Class (v13 Enhanced)

## Spot (Majors: BTC, ETH)

### Multi-Factor Momentum
- Combines SMA/EMA crossover, volume confirmation, and on-chain inflow proxies.
- Regime filter: stronger in trending markets (high ADX proxy).
- Position size adaptive to realized volatility.

### Mean Reversion with Divergence
- RSI/Bollinger extremes + RSI divergence detection.
- Best in ranging regimes. Size reduced in high vol.

## Futures / Perpetuals

### Funding Rate Arbitrage (Enhanced)
- Delta-neutral: long spot / short perp when funding positive (and vice versa).
- Dynamic thresholds based on historical funding distribution.
- Rebalance on basis drift. Includes funding rate forecast proxy.

### Leveraged Trend with Liquidation Distance
- Strict leverage caps. Circuit breaker on funding flips or vol spikes.

## Options (Conceptual)

### Protective Put / Covered Call
- Defined risk. Premium collection or downside protection.
- IV rank proxy for entry timing.

### Volatility Harvesting
- Straddle when IV low relative to realized vol forecast.

## DeFi / On-chain

### Hedged LP Provision
- AMM liquidity + perp hedge. Monitor IL vs fees + on-chain activity.

### Yield Farming Risk-Scored
- Position size by protocol risk score (TVL, audits, historical incidents proxy).

All strategies emit signals that must be approved by the RiskEngine. Strategies are pure and testable.
