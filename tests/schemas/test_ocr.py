#tests/schemas/test_ocr.py

from src.schemas.ocr import BoundingBox, OCRTextBlock, OCRResult

def test_bunding_box_string_to_float():
    bbox = BoundingBox(
        x_min=100,
        y_min="100",
        x_max="200",
        y_max=200,
    )

    assert bbox.x_min == 100
    assert bbox.y_min == 100
    assert bbox.x_max == 200
    assert bbox.y_max == 200


def test_pytest_is_working():
    assert True
