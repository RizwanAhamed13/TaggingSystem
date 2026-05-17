# Repo-Ready Execution Plan

## Proposed folder structure
- `src/taggingsystem/api`: API contracts and endpoints.
- `src/taggingsystem/services`: OCR, tagging, description, storage orchestration.
- `src/taggingsystem/evaluation`: metrics and benchmark runner.
- `src/taggingsystem/datasets`: dataset manifest for benchmark sources.
- `docs/`: architecture, research matrix, dataset/license notes, benchmark template, runbook.
- `tests/`: service and metric behavior checks.

## Service boundaries
- Ingestion API receives files and delegates to pipeline.
- Pipeline coordinates storage, OCR, tagging, and extractive description.
- Repository abstraction stores processed document metadata.
- Evaluation package computes CER/WER, tag F1, throughput.

## API contracts
- `POST /documents`: upload and process document.
- `GET /documents/{document_id}`: retrieve processed record.
- `GET /health`: health endpoint.

## Milestone tickets
1. Replace in-memory repo with PostgreSQL persistence layer.
2. Add MinIO/S3 adapter and artifact metadata schema.
3. Integrate real PaddleOCR/Tesseract/DocTR adapters.
4. Add OpenSearch indexing and search endpoints.
5. Train/evaluate TF-IDF + fastText taggers with benchmark dataset.
6. Add Celery async processing and retry/idempotency controls.
7. Add Prometheus metrics and Grafana dashboard pack.
8. Add human-in-the-loop review UI for tags/descriptions.
