#src/pipeline/receipt_pipeline.py

from src.llm.ollama import OllamaLLM
from src.parsers.receipt_parser import parse_receipt
from src.extraction.pdf_text import extract_text_from_pdf
from src.schemas.receipt import Receipt
from src.validators.register_number import validate_register_number
import json

class ReceiptPipeline:
    """Pipeline for extracting receipt information from a PDF file."""

    def __init__(self, llm=None):
        self.llm = llm if llm else OllamaLLM()

    def run_pdf(self, pdf_path: str) -> Receipt:
        """Extract receipt information from a PDF file."""
        text = extract_text_from_pdf(pdf_path)

        print(f"\nExtracted text: {text}")

        llm_output = self.llm.ocr(text)

        print(f"\nLLM output: {llm_output}")

        # Convert raw llm output to dict
        data = json.loads(llm_output)

        is_register_number_valid = validate_register_number(data["register_number"])

        if not is_register_number_valid:
            # re-run again if it is not valid for 1 more time
            llm_output = self.llm.ocr(text)
            data = json.loads(llm_output)
            is_register_number_valid = validate_register_number(data["register_number"])

        # either it passes the above valid check or this is the second run
        if is_register_number_valid:
            data["need_human_check"] = False
        else:
            data["need_human_check"] = True

        print(f"\nData: {data}")

        receipt = parse_receipt(data)

        print(f"\nParsed receipt: {receipt}")

        return receipt