"""Paper executor: simulation only, no real orders."""

class PaperExecutor:
    def __init__(self, initial_equity: float = 10000.0):
        self.equity = initial_equity
        self.positions = {}

    def execute(self, decision) -> dict:
        if not decision.approved:
            return {"status": "rejected"}
        # Simulate fill
        return {"status": "filled_paper", "size_pct": decision.adjusted_size_pct, "equity": self.equity}
