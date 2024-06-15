import os
import pytest
import sys
from pypdf import PdfWriter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from merger import merge_pdfs

@pytest.fixture
def setup_files(tmp_path):
    for i in range(2):
        test_pdf = tmp_path / f"test_{i}.pdf"
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(test_pdf, "wb") as f:
            writer.write(f)
    return test_pdf

