import pytest
from src.parsers.ocr_parser import parse_ocr_result
from src.schemas.ocr import OCRResult
from pydantic import ValidationError

def test_parse_ocr_result():
    raw = {
    "document_id": "1234567890",
    "page_number": "1",
    "blocks": [
        {

            "text": "Room Area: 45.5 sqm",
            "confidence": "0.95",
            "bbox": {
                "x_min": "0",
                "y_min": "0",
                "x_max": "100",
                "y_max": "100"
            }
        },
        {
            "text": "Meeting Room: Area: 20.5 sqm",
            "confidence": "0.95",
            "bbox": {
                "x_min": "0",
                "y_min": "0",
                "x_max": "100",
                "y_max": "100"
            }
        }
    ]

}

    result = parse_ocr_result(raw)

    # Type check
    assert isinstance(result, OCRResult)


    # Top-level fields
    assert result.document_id == "1234567890"
    assert result.page_number == 1

    # Blocks field
    blocks = result.blocks

    assert len(blocks) == 2
    assert blocks[0].text == "Room Area: 45.5 sqm"
    assert blocks[0].confidence == 0.95
    assert blocks[0].bbox.x_min == 0
    assert blocks[0].bbox.y_min == 0
    assert blocks[0].bbox.x_max == 100
    assert blocks[0].bbox.y_max == 100
    assert blocks[1].text == "Meeting Room: Area: 20.5 sqm"
    assert blocks[1].confidence == 0.95
    assert blocks[1].bbox.x_min == 0
    assert blocks[1].bbox.y_min == 0
    assert blocks[1].bbox.x_max == 100
    assert blocks[1].bbox.y_max == 100

    # Missing blocks field
    raw_with_missing_blocks = {
    "document_id": "1234567890",
    "page_number": "1",
}

    with pytest.raises(ValidationError):
        parse_ocr_result(raw_with_missing_blocks)

    # Missing bbox field
    raw_with_missing_bbox = {
    "document_id": "1234567890",
    "page_number": "1",
    "blocks": [
        {
            "text": "Room Area: 45.5 sqm",
            "confidence": "0.95",
        }
    ]
}
    with pytest.raises(ValidationError):
        parse_ocr_result(raw_with_missing_bbox)

    # Missing confidence field
    raw_with_missing_confidence = {
    "document_id": "1234567890",
    "page_number": "1",
    "blocks": [
        {
            "text": "Room Area: 45.5 sqm",
            "bbox": {
                "x_min": "0",
                "y_min": "0",
                "x_max": "100",
                "y_max": "100"
            }
        }
    ]
}
    result = parse_ocr_result(raw_with_missing_confidence)
    assert result.blocks[0].confidence is None

