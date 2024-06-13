import os
import pytest
import sys
from pypdf import PdfWriter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from splitter import split_pdf


@pytest.fixture
def setup_files(tmp_path):
    test_pdf = tmp_path / "test.pdf"
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(test_pdf, "wb") as f:
        writer.write(f)
    return test_pdf


def test_split(setup_files, tmp_path):
    input_pdf = setup_files
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    split_pdf(input_pdf, output_dir)

    output_files = os.listdir(output_dir)
    assert len(output_files) > 0, "No files were created in the output directory"

    for output_file in output_files:
        assert output_file.endswith('.pdf'), f"Unexpected file type found: {output_file}"
