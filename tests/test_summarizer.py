import pytest

from pdf_digest.summarizer import chunk_text


def test_chunking_preserves_all_characters_and_overlap():
    pieces = chunk_text("abcdefghij", chunk_size=6, overlap=2)
    assert pieces == ["abcdef", "efghij"]


def test_invalid_overlap_is_rejected():
    with pytest.raises(ValueError):
        chunk_text("text", chunk_size=5, overlap=5)
