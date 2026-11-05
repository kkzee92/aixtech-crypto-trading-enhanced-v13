# Architecture Overview (v13)

## Layers
1. **Data Layer**: Synthetic by default; extensible to multi-source OHLCV, funding, orderbook, on-chain proxies.
2. **Strategy Layer**: Modular per asset class. Pure functions/classes that emit Signals with strength, side, and regime.
3. **Risk Engine**: Always between signal and execution. Deterministic gates, volatility-adaptive sizing, anomaly detection, circuit breakers.
4. **Execution Layer**: PaperExecutor only in this version. Extensible but locked to simulation.
5. **Security / Audit**: AuditLogger with hash-chaining simulation. Redaction and zero-trust principles.

## Enhancements in v13
- Regime clustering proxies and volatility forecasting integration into signals and risk.
- Expanded on-chain and funding rate factors.
- Stronger anomaly detection (inflow extremes, vol spikes).
- Full alignment with AI-agent harness practices from zeekiankok92.

## Safety
No live execution paths are implemented. All demos use mock data.
