#src/io/mock_ocr.py
from src.schemas.ocr import OCRResult, OCRTextBlock, BoundingBox

def load_mock_ocr() -> OCRResult:
    return OCRResult(
        page_number=1,
        blocks=[
            OCRTextBlock(text="Room Area: 45.5 sqm", confidence=0.95, bbox=BoundingBox(x_min=0, y_min=0, x_max=100, y_max=100)),
        ],
    )
