# System Design

## Scope
Non-LLM pipeline: ingest documents, OCR/extract text, store source+artifacts, auto-tag, and produce 1-2 line extractive descriptions.

## Target Architecture
- API/Ingestion: FastAPI.
- Async workers: Celery + Redis (optional deployment profile).
- Metadata: PostgreSQL.
- Binary storage: S3/MinIO.
- Search index: OpenSearch (BM25 analyzers).
- OCR engines: PaddleOCR primary, Tesseract/OCRmyPDF alternatives, native PDF extractor fallback.
- Tagging: TF-IDF + linear classifier baseline, fastText option, BM25 keyword expansion.
- Description: TextRank/LexRank style extractive summarization.
- MLOps/ops: MLflow, Prometheus/Grafana, Airflow/Prefect orchestration.

## Service Boundaries
- `api`: upload/retrieve/status contracts.
- `services.ocr`: engine abstraction and fallback routing.
- `services.tagging`: deterministic non-LLM tag prediction.
- `services.description`: extractive summarization only.
- `evaluation`: benchmark runners and KPI metrics.

## API Contracts
- `POST /documents`: accepts multipart file and returns document id, tags, summary, preview.
- `GET /documents/{id}`: fetches processed metadata and outputs.
- `GET /health`: health check.

## Phase Mapping
- A: ingestion/storage/OCR/searchable text.
- B: tagging model training + inference.
- C: extractive description quality improvements.
- D: benchmark suite + dashboards + regression.
- E: hardening: idempotency, auth, audit, rollback.
