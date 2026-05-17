# TaggingSystem

Non-LLM document intelligence platform for OCR, storage, automatic tagging, and 1-2 line extractive description.

## What this repository includes

- FastAPI ingestion API.
- Pluggable OCR pipeline (PaddleOCR/Tesseract/OCRmyPDF adapters and native PDF fallback abstraction).
- Non-LLM tagging service (keyword + optional TF-IDF classifier hooks).
- Extractive 1-2 line description generator.
- Benchmark/evaluation scaffolding (OCR, tagging, description, throughput metrics).
- Documentation package: architecture, OSS comparison, dataset card, benchmark report template, and runbook.

## Quick start

```bash
python -m pip install -e .[dev]
uvicorn taggingsystem.main:app --reload
pytest
```

## API

- `GET /health`
- `POST /documents` (multipart `file`, optional `filename`)
- `GET /documents/{document_id}`
