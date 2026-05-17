from collections.abc import Iterable


def cer(reference: str, hypothesis: str) -> float:
    return _levenshtein_rate(list(reference), list(hypothesis))


def wer(reference: str, hypothesis: str) -> float:
    return _levenshtein_rate(reference.split(), hypothesis.split())


def precision_recall_f1_at_k(true_labels: set[str], predicted_labels: list[str], k: int = 5) -> dict[str, float]:
    top = set(predicted_labels[:k])
    tp = len(true_labels & top)
    precision = tp / len(top) if top else 0.0
    recall = tp / len(true_labels) if true_labels else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}


def throughput_docs_per_min(count: int, elapsed_seconds: float) -> float:
    if elapsed_seconds <= 0:
        return 0.0
    return count * 60.0 / elapsed_seconds


def _levenshtein_rate(reference: Iterable[str], hypothesis: Iterable[str]) -> float:
    ref = list(reference)
    hyp = list(hypothesis)
    if not ref:
        return 0.0 if not hyp else 1.0

    dp = [[0] * (len(hyp) + 1) for _ in range(len(ref) + 1)]
    for i in range(len(ref) + 1):
        dp[i][0] = i
    for j in range(len(hyp) + 1):
        dp[0][j] = j

    for i, r in enumerate(ref, start=1):
        for j, h in enumerate(hyp, start=1):
            cost = 0 if r == h else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[-1][-1] / len(ref)
