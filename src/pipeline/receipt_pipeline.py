#src/pipeline/receipt_pipeline.py

from src.llm.ollama import OllamaLLM
from src.parsers.receipt_parser import parse_receipt
from src.extraction.pdf_text import extract_text_from_pdf
from src.schemas.receipt import Receipt
from src.validators.amount import validate_amount
from src.validators.register_number import validate_register_number
import json
from src.extraction.image_text import extract_text_from_image

class ReceiptPipeline:
    """Pipeline for extracting receipt information from a PDF file."""

    def __init__(self, llm=None):
        self.llm = llm if llm else OllamaLLM()

    def run(self, file_path: str) -> Receipt:
        """Extract receipt information from a file."""
        ext = file_path.rsplit(".", 1)[-1].lower()

        if ext == "pdf":
            return self.run_pdf(file_path)
        elif ext in ("jpg", "jpeg", "png"):
            return self.run_image(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    def run_pdf(self, pdf_path: str) -> Receipt:
        """Extract receipt information from a PDF file."""
        text = extract_text_from_pdf(pdf_path)

        llm_output = self.llm.ocr(text)

        # Convert raw llm output to dict
        data = json.loads(llm_output)

        is_register_number_valid = validate_register_number(data["register_number"])
        is_amount_valid = validate_amount(data["amount"])

        if not is_register_number_valid or not is_amount_valid:
            # re-run again if it is not valid for 1 more time
            llm_output = self.llm.ocr(text)
            data = json.loads(llm_output)
            is_register_number_valid = validate_register_number(data["register_number"])
            is_amount_valid = validate_amount(data["amount"])

        # either it passes the above valid check or this is the second run
        if is_register_number_valid and is_amount_valid:
            data["need_human_check"] = False
        else:
            data["need_human_check"] = True

        data['file_type'] = 'pdf'
        
        data['file_path'] = pdf_path

        receipt = parse_receipt(data)

        return receipt

    def run_image(self, image_path: str) -> Receipt:

        text = extract_text_from_image(image_path)

        llm_output = self.llm.ocr(text)

        # Convert raw llm output to dict
        data = json.loads(llm_output)

        is_register_number_valid = validate_register_number(data["register_number"])
        is_amount_valid = validate_amount(data["amount"])

        if not is_register_number_valid or not is_amount_valid:
            # re-run again if it is not valid for 1 more time
            llm_output = self.llm.ocr(text)
            data = json.loads(llm_output)
            is_register_number_valid = validate_register_number(data["register_number"])
            is_amount_valid = validate_amount(data["amount"])

        # either it passes the above valid check or this is the second run
        if is_register_number_valid and is_amount_valid:
            data["need_human_check"] = False
        else:
            data["need_human_check"] = True

        data['file_type'] = 'image'

        data['file_path'] = image_path

        receipt = parse_receipt(data)

        return receipt
