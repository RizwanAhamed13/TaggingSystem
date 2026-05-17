# Dataset Card (Educational + Document Intelligence Bench)

## Objective
Build a balanced benchmark across scanned and born-digital educational/scientific documents for OCR, auto-tagging, and extractive description.

## Candidate datasets
- arXiv OA subsets (born-digital PDFs)
- PubMed Central OA subsets (domain variation)
- S2ORC slices (metadata + corpus scale)
- DocLayNet (layout stress)
- RVL-CDIP / IIT-CDIP subsets (document diversity)
- FUNSD (forms, key-value extraction stress)
- Open educational policy/books/course PDFs from permissive licenses

## Split design
- By modality: scanned vs native PDF.
- By complexity: single column, multi-column, tables/forms, low-quality scan.
- By domain: science, education policy, institutional docs.

## Licensing policy
Only include permissive/open subsets. Preserve attribution, redistribution terms, and source URLs in manifest.
