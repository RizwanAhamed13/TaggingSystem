from pathlib import Path

from taggingsystem.evaluation.metrics import cer, precision_recall_f1_at_k, wer
from taggingsystem.services.description import DescriptionService
from taggingsystem.services.pipeline import DocumentPipeline
from taggingsystem.services.tagging import TaggingService


def test_tagging_service_predicts_domain_tags() -> None:
    service = TaggingService()
    text = "This education policy document describes curriculum reform and teacher training."
    tags = service.predict(text)
    assert "education" in tags
    assert "policy" in tags


def test_description_service_extracts_short_summary() -> None:
    service = DescriptionService(max_sentences=2)
    text = (
        "This report evaluates student learning outcomes in public schools. "
        "It compares curriculum interventions across districts. "
        "Appendices include supplemental tables."
    )
    summary = service.summarize(text)
    assert len(summary) > 0
    assert summary.count(".") <= 3


def test_pipeline_ingest_returns_outputs(tmp_path: Path) -> None:
    from taggingsystem.config import settings

    settings.local_storage_dir = str(tmp_path)
    pipeline = DocumentPipeline()
    content = b"Education research dataset and methodology for school improvement."
    result = pipeline.ingest("sample.pdf", content)
    assert result.text
    assert result.tags
    assert result.description


def test_metrics_basic_values() -> None:
    assert cer("abc", "abc") == 0
    assert wer("hello world", "hello world") == 0
    stats = precision_recall_f1_at_k({"a", "b"}, ["a", "c"], k=2)
    assert stats["precision"] == 0.5
    assert stats["recall"] == 0.5
