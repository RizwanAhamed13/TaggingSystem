from dataclasses import dataclass
from time import perf_counter

from taggingsystem.evaluation.metrics import cer, precision_recall_f1_at_k, throughput_docs_per_min, wer
from taggingsystem.services.pipeline import DocumentPipeline


@dataclass(slots=True)
class BenchmarkSample:
    filename: str
    content: bytes
    expected_text: str
    expected_tags: set[str]


class BenchmarkRunner:
    def __init__(self, pipeline: DocumentPipeline) -> None:
        self.pipeline = pipeline

    def run(self, samples: list[BenchmarkSample]) -> dict[str, float]:
        if not samples:
            return {"cer": 0.0, "wer": 0.0, "tag_f1": 0.0, "docs_per_min": 0.0}

        started = perf_counter()
        total_cer = total_wer = total_f1 = 0.0
        for sample in samples:
            record = self.pipeline.ingest(sample.filename, sample.content)
            total_cer += cer(sample.expected_text, record.text)
            total_wer += wer(sample.expected_text, record.text)
            total_f1 += precision_recall_f1_at_k(sample.expected_tags, record.tags, k=5)["f1"]
        elapsed = perf_counter() - started

        n = len(samples)
        return {
            "cer": total_cer / n,
            "wer": total_wer / n,
            "tag_f1": total_f1 / n,
            "docs_per_min": throughput_docs_per_min(n, elapsed),
        }
