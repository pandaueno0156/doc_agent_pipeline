import logging

def setup_logging(level=logging.WARNING):

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # Suppress noisy pdfminer font warnings (used by pdfplumber)
    logging.getLogger("pdfminer").setLevel(logging.ERROR)