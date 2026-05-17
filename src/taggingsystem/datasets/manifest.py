from dataclasses import dataclass


@dataclass(slots=True)
class DatasetEntry:
    name: str
    source: str
    license: str
    modality: str
    purpose: str


DATASET_MANIFEST: list[DatasetEntry] = [
    DatasetEntry(
        name="arXiv Open Access",
        source="https://info.arxiv.org/help/bulk_data_s3.html",
        license="Various by article (OA subset only)",
        modality="Born-digital scientific PDFs",
        purpose="OCR fallback and extractive summary benchmarking",
    ),
    DatasetEntry(
        name="PubMed Central Open Access",
        source="https://pmc.ncbi.nlm.nih.gov/tools/openftlist/",
        license="Open access subset",
        modality="Biomedical full-text PDFs/XML",
        purpose="Tagging and domain robustness",
    ),
    DatasetEntry(
        name="DocLayNet",
        source="https://github.com/DS4SD/DocLayNet",
        license="CC BY 4.0",
        modality="Page layout annotations",
        purpose="Layout-aware OCR validation",
    ),
    DatasetEntry(
        name="FUNSD",
        source="https://guillaumejaume.github.io/FUNSD/",
        license="Research dataset license",
        modality="Scanned forms with labels",
        purpose="Form/table OCR stress tests",
    ),
    DatasetEntry(
        name="RVL-CDIP",
        source="https://www.cs.cmu.edu/~aharley/rvl-cdip/",
        license="Academic/research terms",
        modality="Document image classification corpus",
        purpose="Document-type tagging stress test",
    ),
]
