from src.pipeline.receipt_pipeline import ReceiptPipeline
from src.config.logging_config import setup_logging

def main():

    setup_logging()

    pdf_path = "tests/data/receipt1.pdf"

    pipeline = ReceiptPipeline()

    receipt = pipeline.run_pdf(pdf_path)
    
    print(f"\nExtracted Receipt: {receipt}")

    print("\nAs dict:")
    receipt_dict = receipt.model_dump()
    print(receipt_dict)

if __name__ == "__main__":
    main()