from src.pipeline.receipt_pipeline import ReceiptPipeline
from src.config.logging_config import setup_logging
import os
from src.io.csv_writer import save_receipt_to_csv
import time
import argparse

# python -m main

def parse_args():
    parser = argparse.ArgumentParser(description="Extract taxi reciepts and transform into csv file.")
    parser.add_argument(
        "--output",
        type=str,
        default="output/receipts.csv",
        help="Output path for the csv file"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data",
        help="Input data directory for OCR processing"
    )
    return parser.parse_args()

def main():

    setup_logging()

    args = parse_args()

    pipeline = ReceiptPipeline()

    results = []
    
    current_time = time.time()

    input_data_dir = args.input

    for filename in os.listdir(input_data_dir):
        file_path = os.path.join(input_data_dir, filename)

        if not os.path.isfile(file_path):
            continue

        print(f"\n{'-'*50}")
        print(f"\n Processing file: {filename}\n")

        current_file_time = time.time()

        try:
            receipt = pipeline.run(file_path)
            
            print(f"\nExtracted Receipt: {receipt}")

            receipt_dict = receipt.model_dump()

            print(receipt_dict)

            results.append(receipt_dict)

            end_processing_time = time.time()

            total_processing_time_single_file = end_processing_time - current_file_time

            print(f"\nTotal time taken for {filename}: {total_processing_time_single_file} seconds\n")

        except ValueError as e:
            print(f"Skipping {filename}: {e}")

    # sort the results based on the logic as below:
    # transactional date comes first
    # image file type should come first
    # cheaper amount should come first 
    results.sort(key=lambda r: (r["transaction_date"], r["file_type"]!= "image", r["amount"]))
    
    # save results as csv
    save_receipt_to_csv(results, output_path=args.output)
    
    # Total process time
    end_time = time.time()
    print(f"\nTotal time taken: {end_time - current_time} seconds\n")

if __name__ == "__main__":
    main()