# AGENTS.md - Rules for AI Coding Agents

This repository follows safe AI-agent practices inspired by zeekiankok92/aixtech-agent-harness-demo.

## Core Rules
- All trading logic is paper/simulation only. Never implement live order execution with real funds without explicit human approval and separate review.
- Use only synthetic or public market data. Never include real API keys, private keys, mnemonics, or user PII.
- Every signal must pass through the RiskEngine before any execution path.
- Commit messages must disclose AI assistance if used.
- Changes to risk, security, or execution modules require human review (see harness/review-checklist.md if present).
- Prefer pure functions for strategies. Keep side effects in execution and audit layers.

## Security
- Redact secrets in all logs and outputs.
- Audit logs must be append-only and hash-chained where possible.
- No withdrawal or transfer permissions in any API key examples.

## Testing
- Include unit tests for risk gates and strategy signals.
- Run with synthetic data in CI.
