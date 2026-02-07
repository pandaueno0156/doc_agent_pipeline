#src/schemas/document.py

from pydantic import BaseModel
from typing import List, Optional

class DocumentMetadata(BaseModel):
    document_id: str
    total_page_count: int
    source: Optional[str] = None
