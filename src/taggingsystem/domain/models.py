from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(slots=True)
class DocumentRecord:
    filename: str
    storage_uri: str
    text: str
    tags: list[str]
    description: str
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: UUID = field(default_factory=uuid4)
