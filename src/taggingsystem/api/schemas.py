from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    storage_uri: str
    text_preview: str = Field(description="First 280 chars of extracted text")
    tags: list[str]
    description: str
    created_at: datetime


class HealthResponse(BaseModel):
    status: str
