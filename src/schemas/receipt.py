#src/schemas/receipt.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class Receipt(BaseModel):

    register_number: str = Field(...,description="The register number of the taxi")

    transaction_date: date = Field(...,description="Transcation date in YYYY-MM-DD format")

    amount: int = Field(..., description="Total amount in yen")

    vendor: Optional[str] = Field(None, description="Taxi company name")

    need_human_check: bool = Field(..., description="Whether the receipt needs human check")

