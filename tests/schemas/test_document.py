#tests/schemas/test_document.py

from src.schemas.document import DocumentMetadata

def test_document_metadata_valid():
    metadata = DocumentMetadata(
        document_id="123",
        total_page_count="10",
        source="pdf"
            )

    assert metadata.total_page_count == 10 # even if it is stored as 10 string, it can be converted to 10 int
    assert metadata.source == "pdf"


def test_document_metadata_optional_source():
    metadata = DocumentMetadata(
        document_id="123",
        total_page_count="10"
            )

    assert metadata.source is None

