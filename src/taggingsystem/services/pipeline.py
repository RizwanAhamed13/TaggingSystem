from taggingsystem.config import settings
from taggingsystem.domain.models import DocumentRecord
from taggingsystem.services.description import DescriptionService
from taggingsystem.services.ocr import OCRService
from taggingsystem.services.storage import LocalStorage
from taggingsystem.services.tagging import TaggingService


class InMemoryDocumentRepository:
    def __init__(self) -> None:
        self._store: dict[str, DocumentRecord] = {}

    def save(self, doc: DocumentRecord) -> DocumentRecord:
        self._store[str(doc.id)] = doc
        return doc

    def get(self, document_id: str) -> DocumentRecord | None:
        return self._store.get(document_id)


class DocumentPipeline:
    def __init__(self) -> None:
        self.storage = LocalStorage(settings.local_storage_dir)
        self.ocr = OCRService(primary_engine=settings.default_ocr_engine)
        self.tagging = TaggingService()
        self.description = DescriptionService(max_sentences=settings.max_description_sentences)
        self.repo = InMemoryDocumentRepository()

    def ingest(self, filename: str, content: bytes) -> DocumentRecord:
        storage_uri = self.storage.save(filename, content)
        ocr_result = self.ocr.extract_text(content, filename)
        text = ocr_result.text.strip()
        tags = self.tagging.predict(text)
        summary = self.description.summarize(text)
        record = DocumentRecord(
            filename=filename,
            storage_uri=storage_uri,
            text=text,
            tags=tags,
            description=summary,
            metadata={"ocr_engine": ocr_result.engine, "ocr_confidence": ocr_result.confidence},
        )
        return self.repo.save(record)
