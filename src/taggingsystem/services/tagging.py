import math
import re
from collections import Counter


TOKEN = re.compile(r"[a-zA-Z0-9]{2,}")


class TaggingService:
    """Non-LLM auto-tagging: keyword+term-frequency scorer with deterministic output."""

    def __init__(self) -> None:
        self.taxonomy: dict[str, set[str]] = {
            "education": {"education", "school", "student", "curriculum", "learning", "teacher"},
            "research": {"research", "study", "method", "results", "dataset", "experiment"},
            "policy": {"policy", "regulation", "compliance", "governance", "framework"},
            "finance": {"budget", "financial", "cost", "revenue", "funding", "expense"},
            "health": {"health", "clinical", "patient", "medical", "treatment"},
            "technology": {"software", "system", "algorithm", "model", "architecture", "data"},
        }

    def _tokens(self, text: str) -> list[str]:
        return [t.lower() for t in TOKEN.findall(text)]

    def predict(self, text: str, top_k: int = 5) -> list[str]:
        tokens = self._tokens(text)
        if not tokens:
            return ["unclassified"]
        counts = Counter(tokens)
        norm = math.sqrt(sum(v * v for v in counts.values())) or 1.0
        scored: list[tuple[str, float]] = []
        for tag, vocab in self.taxonomy.items():
            score = sum(counts[w] for w in vocab if w in counts) / norm
            if score > 0:
                scored.append((tag, score))
        if not scored:
            return ["general"]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [tag for tag, _ in scored[:top_k]]
