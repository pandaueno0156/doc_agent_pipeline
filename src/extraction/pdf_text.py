#src/extraction/pdf_text.py

import pdfplumber

def clean_text(text: str) -> str:
    return text.replace("\n\n", "\n").strip()

def extract_text_from_pdf(pdf_path: str) -> str:

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    # clean text
    text = clean_text(text)

    return text


# text = extract_text_from_pdf("tests/data/receipt1.pdf")
# text = clean_text(text)
# print(text)