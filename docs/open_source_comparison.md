# Open-Source Comparison Matrix

## OCR
| Tool | Strengths | Weaknesses | Fit |
|---|---|---|---|
| PaddleOCR | Strong multilingual OCR, robust layout scenarios | Heavier runtime/GPU tuning | Primary OCR engine |
| Tesseract | Mature, lightweight CPU usage | Lower quality on noisy layouts | Cost-efficient fallback |
| EasyOCR | Fast setup, broad language support | Accuracy variance on dense docs | Prototyping/ablation |
| OCRmyPDF | Excellent searchable PDF pipeline | Focused on PDFs only | PDF enhancement stage |
| DocTR | Deep-learning document OCR, detection+recognition | Larger dependency stack | Layout-aware OCR benchmark |

## Document understanding
| Tool | Strengths | Weaknesses | Fit |
|---|---|---|---|
| GROBID | Best-in-class scholarly structure extraction | Academic PDF focus | Research corpora parsing |
| Apache Tika | Broad format support | Layout semantics limited | Generic text extraction fallback |
| Unstructured | Rich partition strategies | More moving parts | Enterprise preprocessing |

## Tagging and Search
| Tool | Strengths | Weaknesses | Fit |
|---|---|---|---|
| scikit-learn TF-IDF + Linear | Fast, interpretable, strong baseline | Needs retraining per taxonomy drift | Baseline classifier |
| fastText | Efficient supervised text classification | Weaker contextual nuance | High-throughput classifier |
| OpenSearch BM25 | Strong lexical retrieval | Not classifier by itself | Candidate tag expansion |

## Extractive summarization
| Tool | Strengths | Weaknesses | Fit |
|---|---|---|---|
| sumy (LexRank/TextRank) | Deterministic extractive summaries | Limited discourse awareness | No-LLM summary baseline |
| spaCy sentence scoring | Flexible rule-driven scoring | Requires feature engineering | Domain tuning layer |
