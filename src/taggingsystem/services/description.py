import re
from collections import Counter


SPLIT = re.compile(r"(?<=[.!?])\s+")
TOKEN = re.compile(r"[a-zA-Z0-9]{2,}")
STOP = {
    "the", "and", "for", "that", "with", "this", "from", "into", "their", "were", "have", "has", "been",
    "are", "is", "of", "to", "in", "on", "a", "an", "by", "as", "it", "at", "or", "be",
}


def _ranked_sentence_items(sentences: list[str], frequencies: Counter[str], scorer: "DescriptionService") -> list[tuple[int, float, str]]:
    return [(idx, scorer._sentence_score(sentence, frequencies), sentence) for idx, sentence in enumerate(sentences)]


class DescriptionService:
    """Extractive 1-2 sentence summarizer without any generative model."""

    def __init__(self, max_sentences: int = 2) -> None:
        self.max_sentences = max(1, max_sentences)

    def _sentence_score(self, sentence: str, frequencies: Counter[str]) -> float:
        words = [w.lower() for w in TOKEN.findall(sentence) if w.lower() not in STOP]
        if not words:
            return 0.0
        return sum(frequencies[w] for w in words) / len(words)

    def summarize(self, text: str) -> str:
        sentences = [s.strip() for s in SPLIT.split(text.strip()) if s.strip()]
        if not sentences:
            return "No extractable description available."

        tokens = [w.lower() for w in TOKEN.findall(text) if w.lower() not in STOP]
        freqs = Counter(tokens)
        ranked = sorted(_ranked_sentence_items(sentences, freqs, self), key=lambda item: item[1], reverse=True)
        chosen = sorted(ranked[: self.max_sentences], key=lambda x: x[0])
        summary = " ".join(s for _, _, s in chosen)
        if len(summary) > 400:
            summary = summary[:397].rstrip() + "..."
        return summary
