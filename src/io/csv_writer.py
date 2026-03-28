import csv 
import os
from datetime import date

def save_receipt_to_csv(receipts: list[dict], output_path: str="output/receipts.csv"):
    if not receipts:
        print("No receipt to save.")
        return
    
    # make file path upto output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # extract columns from dictionary
    column_names = receipts[0].keys()

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=column_names)
        # write columns to first row
        writer.writeheader()
        # write dict data to each rows from list (receipts)
        writer.writerows(receipts)

    print(f"\nSaved {len(receipts)} receipts to {output_path}")