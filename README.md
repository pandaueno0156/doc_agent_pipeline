# Doc_agent_pipeline


# Goal
A processing pipeline that extracts structured data from Japanese taxi receipts (PDF and photo images) and outputs a CSV file for expense reporting.

# Backgound
Building this pipeline to automate the extraction and produce a CSV that I can reference when filing my traveling expenses for work.

# How it works
1. Place all receipt files (PDF and JPG/PNG) into the data/ folder.
2. Run the pipeline. For each file:
- PDFs: text is extracted using pdfplumber.
- Images: text is extracted using PaddleOCR (PP-OCRv5, Japanese).
- The extracted text is sent to a local LLM (Ollama) which returns structured JSON with the transaction date, amount, and register number.
- The register number and amount are validated. If validation fails, the LLM is called once more. If it still fails, the record is flagged for manual review.
3. All results are sorted by date, then by file type (image before PDF), then by amount.
4. The sorted results are written to a CSV file.

# Project structure

```
src/
├── config/
│   ├── logging_config.py        -- logging setup, suppresses pdfminer warnings
│   └── settings.py              -- environment variables and app config
├── extraction/
│   ├── image_text.py            -- OCR text extraction from images using PaddleOCR
│   └── pdf_text.py              -- text extraction from PDFs using pdfplumber
├── io/
│   └── csv_writer.py            -- writes receipt records to CSV
├── llm/
│   ├── base.py                  -- abstract base class for LLM implementations
│   └── ollama.py                -- Ollama LLM integration with JSON extraction prompt
├── parsers/
│   └── receipt_parser.py        -- converts LLM JSON output into Receipt objects
├── pipeline/
│   └── receipt_pipeline.py      -- main pipeline tying extraction, LLM, validation, and parsing
├── schemas/
│   └── receipt.py               -- Pydantic data model for a taxi receipt
└── validators/
    ├── amount.py                -- validates fare is divisible by 10
    └── register_number.py       -- validates register number format (T + 13 digits)
```

# How to use
1. Basic usage (reads from data/, writes to output/receipts.csv):

`python -m main`

2. Custom input and output:

`python -m main --input data --output output/march-expenses.csv`
