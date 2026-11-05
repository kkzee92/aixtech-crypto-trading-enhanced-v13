# Security Architecture

## Zero-Trust Principles
- Least privilege: API keys (if ever used) are read + trade only. No withdraw, no transfer.
- Secrets never committed. Use environment variables or external vaults.
- All inputs validated and sanitized. Expanded redaction for private keys, BIP39 seeds, API tokens, AWS keys, etc.
- Immutable audit trail: JSONL logs with timestamps, event types, and optional SHA256 chaining for integrity.

## Data Protection
- Default to synthetic data for development and CI.
- No real user PII. Aligns with PDPA-style practices from related harness demos.
- Encryption helpers available for sensitive intermediate data (simulation only).

## Risk Controls
- Pre-trade deterministic gates that can veto any signal.
- Circuit breakers for volatility, consecutive losses, data staleness.
- Position size, leverage, and drawdown limits configurable and enforced.

## Reporting
If you discover a security issue, please open a private issue or contact the maintainer. Do not disclose publicly until addressed.
