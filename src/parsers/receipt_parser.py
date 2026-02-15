#src/parsers/receipt_parser.py

from src.schemas.receipt import Receipt
import json

def parse_receipt(raw: str | dict) -> Receipt:
    """
    Parse raw LLM output into a validated Receipt object.

    Args:
        raw: Raw dictionary output from LLM.

    Returns:
        Receipt: Validated receipt object.

    Raises:
        ValidationError: If input data is invalid or incomplete.
    """
    # if the LLM raw output is a string instead of dict
    if isinstance(raw, str):
        raw = json.loads(raw)
    
    # unpack dict values and pass to Receipt object for the key-value
    return Receipt(**raw)