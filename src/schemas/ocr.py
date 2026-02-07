#src/schemas/ocr.py
from pydantic import BaseModel
from typing import List, Optional

class BoundingBox(BaseModel):
    x_min: float
    y_min: float
    x_max: float
    y_max: float

class OCRTextBlock(BaseModel):
    text: str
    confidence: Optional[float] = None
    bbox: BoundingBox

class OCRResult(BaseModel):
    document_id: str
    page_number: int
    blocks: List[OCRTextBlock]
