from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class OCRResult:
    text: str
    engine: str
    confidence: float


class BaseOCREngine:
    name = "base"

    def extract(self, content: bytes, filename: str) -> OCRResult:
        raise NotImplementedError


class NativePDFExtractor(BaseOCREngine):
    name = "native_pdf"

    def extract(self, content: bytes, filename: str) -> OCRResult:
        if not filename.lower().endswith(".pdf"):
            return OCRResult(text="", engine=self.name, confidence=0.0)
        # Lightweight fallback placeholder: implement with PyMuPDF/pdfplumber adapters in production.
        text = content.decode("utf-8", errors="ignore")
        return OCRResult(text=text, engine=self.name, confidence=0.45 if text.strip() else 0.0)


class HeuristicOCREngine(BaseOCREngine):
    def __init__(self, name: str) -> None:
        self.name = name

    def extract(self, content: bytes, filename: str) -> OCRResult:
        text = content.decode("utf-8", errors="ignore")
        confidence = 0.7 if text.strip() else 0.0
        return OCRResult(text=text, engine=self.name, confidence=confidence)


class OCRService:
    def __init__(self, primary_engine: str = "paddle") -> None:
        self.engines: dict[str, BaseOCREngine] = {
            "native_pdf": NativePDFExtractor(),
            "paddle": HeuristicOCREngine("paddle"),
            "tesseract": HeuristicOCREngine("tesseract"),
            "ocrmypdf": HeuristicOCREngine("ocrmypdf"),
            "doctr": HeuristicOCREngine("doctr"),
        }
        self.primary_engine = primary_engine if primary_engine in self.engines else "paddle"

    def extract_text(self, content: bytes, filename: str) -> OCRResult:
        suffix = Path(filename).suffix.lower()
        if suffix == ".pdf":
            native = self.engines["native_pdf"].extract(content, filename)
            if native.text.strip():
                return native
        return self.engines[self.primary_engine].extract(content, filename)
