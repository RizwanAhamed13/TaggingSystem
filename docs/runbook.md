# Runbook

## Deploy
1. Provision PostgreSQL, Redis, OpenSearch, MinIO/S3.
2. Deploy API service (FastAPI).
3. Deploy worker service (Celery).
4. Configure environment variables for storage/search/OCR engine selection.

## Operate
- Monitor queue latency, OCR processing time, and docs/min.
- Monitor tag F1 drift on rolling validation sets.
- Alert on OCR confidence collapse and storage/index failures.

## Retrain
1. Snapshot labeled corrections.
2. Train tagging model candidate.
3. Evaluate against benchmark suite.
4. Register model version and promote via canary rollout.

## Rollback
- Revert model version in registry.
- Requeue affected jobs if needed.
- Restore index snapshot if schema migration impacted retrieval.
