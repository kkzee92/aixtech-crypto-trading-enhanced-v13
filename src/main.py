"""Main entry point for AIxTech Crypto Trading System Enhanced v13. Paper/simulation only."""

import argparse
from datetime import datetime
from src.risk.risk_engine import RiskEngine
from src.security.audit import AuditLogger
from src.strategies.spot.momentum import SpotMomentumStrategy
from src.strategies.futures.funding_arb import FundingArbStrategy
from src.execution.paper import PaperExecutor


def main():
    parser = argparse.ArgumentParser(description="AIxTech Crypto Trading System v13 (paper only)")
    parser.add_argument("--mode", choices=["paper"], default="paper")
    parser.add_argument("--strategy", default="spot_momentum", choices=["spot_momentum", "funding_arb"])
    parser.add_argument("--symbol", default="BTC/USDT")
    parser.add_argument("--equity", type=float, default=10000.0)
    args = parser.parse_args()

    audit = AuditLogger(log_path="logs/audit.jsonl")
    risk = RiskEngine(
        max_position_pct=0.05,
        max_daily_loss_pct=0.03,
        max_leverage=2.0,
        volatility_adaptive=True,  # v13 enhancement
    )
    executor = PaperExecutor(initial_equity=args.equity)

    if args.strategy == "spot_momentum":
        strategy = SpotMomentumStrategy(symbol=args.symbol)
    else:
        strategy = FundingArbStrategy(symbol=args.symbol)

    print(f"Starting paper mode | strategy={args.strategy} | symbol={args.symbol}")
    audit.log("system_start", {"strategy": args.strategy, "symbol": args.symbol, "version": "v13"})

    # Demo with enhanced multi-factor mock data
    for i in range(5):
        mock_data = {
            "price": 65000 + i * 150,
            "volume": 1000 + i * 50,
            "funding_rate": 0.0001 * (1 if i % 2 == 0 else -1),
            "onchain_inflow": 50 - i * 10,  # proxy
            "volatility": 0.02 + i * 0.005,
        }
        signal = strategy.generate_signal(mock_data)
        audit.log("signal", {"iteration": i, "signal": signal.to_dict(), "regime": getattr(signal, "regime", "unknown")})

        decision = risk.evaluate(signal, current_equity=args.equity, current_positions={}, market_data=mock_data)
        audit.log("risk_decision", {"iteration": i, "decision": decision.to_dict()})

        if decision.approved:
            result = executor.execute(decision)
            audit.log("execution", {"iteration": i, "result": result})
            print(f"[{i}] {signal.side} | Regime: {getattr(signal, 'regime', 'N/A')} | Risk: {decision.reason} | Exec: {result.get('status')}")
        else:
            print(f"[{i}] {signal.side} | REJECTED: {decision.reason}")

    print("Demo complete. Check logs/audit.jsonl for hash-chained trail.")
    audit.log("system_stop", {"timestamp": datetime.utcnow().isoformat()})


if __name__ == "__main__":
    main()
