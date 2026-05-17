from functools import lru_cache

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from taggingsystem.api.schemas import DocumentResponse, HealthResponse
from taggingsystem.services.pipeline import DocumentPipeline


router = APIRouter()


@lru_cache(maxsize=1)
def get_pipeline() -> DocumentPipeline:
    return DocumentPipeline()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.post("/documents", response_model=DocumentResponse)
async def ingest_document(
    file: UploadFile = File(...), pipeline: DocumentPipeline = Depends(get_pipeline)
) -> DocumentResponse:
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")
    record = pipeline.ingest(filename=file.filename or "unnamed", content=content)
    return DocumentResponse(
        id=record.id,
        filename=record.filename,
        storage_uri=record.storage_uri,
        text_preview=record.text[:280],
        tags=record.tags,
        description=record.description,
        created_at=record.created_at,
    )


@router.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: str, pipeline: DocumentPipeline = Depends(get_pipeline)) -> DocumentResponse:
    record = pipeline.repo.get(document_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return DocumentResponse(
        id=record.id,
        filename=record.filename,
        storage_uri=record.storage_uri,
        text_preview=record.text[:280],
        tags=record.tags,
        description=record.description,
        created_at=record.created_at,
    )
