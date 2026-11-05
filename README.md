# AIxTech Crypto Trading System Enhanced v13

> Enhanced paper-only automated cryptocurrency trading information system with multi-factor adaptive strategies per asset class, refined regime clustering, volatility forecasting proxies, on-chain and funding rate integration, expanded anomaly detection, and strengthened zero-trust cyber and data security architecture. Research and educational purposes only. No live order execution.

**Disclaimer:** Research only. Cryptocurrency trading involves substantial risk of loss. This system uses synthetic/mock data by default and is designed for backtesting, simulation, and information gathering. Never use with real funds or live APIs with trading permissions without thorough independent review. No financial advice.

## Overview
Builds on previous versions (including v12, secure-crypto-trading-engine) and the AI coding-agent harness from [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo). Key enhancements in v13:

- **Asset-class specific multi-factor strategies**: Majors (BTC/ETH), Large Alts, DeFi tokens, Stablecoins, High-Volatility pairs, Futures/Perps, Options conceptual, DeFi yield.
- **Advanced regime detection**: Volatility clustering proxies, trend strength (ADX-like), market regime filters (trending vs ranging).
- **On-chain and funding proxies**: Simulated exchange inflows, funding rate signals for arb and regime awareness.
- **Enhanced risk gates**: Position sizing adaptive to volatility, correlation checks, drawdown circuit breakers, anomaly (z-score, kurtosis) detection.
- **Strengthened zero-trust security**: Expanded secret redaction (mnemonics, private keys, API keys, seeds), hash-chained immutable audit logs, input sanitization, least-privilege design.
- **Synthetic data mode**: Default for safe CI and AI-agent development.
- **AI-agent harness alignment**: AGENTS.md rules, human review requirements, disclosure trails.

## Quick Start
```bash
git clone https://github.com/kkzee92/aixtech-crypto-trading-enhanced-v13.git
cd aixtech-crypto-trading-enhanced-v13
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.main --mode paper --strategy spot_momentum --symbol BTC/USDT
```

## Architecture
Modular layers: Data ingestion (synthetic or multi-source), Strategy (per asset class pure functions/classes), Risk Engine (always veto-capable), Execution (paper only by default), Security/Audit (immutable JSONL logs with chaining).

See [docs/architecture.md](docs/architecture.md) and [SECURITY.md](SECURITY.md).

## Strategies per Asset Class
See [docs/strategies.md](docs/strategies.md) for detailed logic, regime suitability, and enhancement ideas (e.g., multi-TF confirmation, volume profile, IV rank for options).

## Security Highlights
- No withdrawal permissions ever.
- Secrets via env / vault only.
- Pre-trade deterministic gates.
- Full audit trail with timestamps and hashes.
- PDPA-inspired: synthetic fixtures, no real PII.

## Contributing
Follow AGENTS.md for AI-assisted development. All changes require human review. Use synthetic data.

## License
MIT
