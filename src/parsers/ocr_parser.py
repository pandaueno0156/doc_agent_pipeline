#src/parsers/ocr_parser.py

from src.schemas.ocr import OCRResult

def parse_ocr_result(raw: dict) -> OCRResult:
    """
    Parse raw OCR JSON into a validated OCRResult object.

    Args:
        raw: Raw OCR output dictionary from LLM or OCR engine.

    Returns:
        OCRResult: Validated OCR result.

    Raises:
        ValidationError: If input data is invalid or incomplete.
    """
    # unpack dict values and pass to OCRResult object for the key-value
    return OCRResult(**raw)