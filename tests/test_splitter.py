import os
import pytest
import sys
from pypdf import PdfWriter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from splitter import split_pdf


@pytest.fixture
def create_pdf(tmp_path):
    def _create_pdf(size=(72, 72), num_pages=1):
        pdf_path = tmp_path / f"test_{size[0]}x{size[1]}_{num_pages}pages.pdf"
        writer = PdfWriter()
        for _ in range(num_pages):
            writer.add_blank_page(width=size[0], height=size[1])
        with pdf_path.open("wb") as f:
            writer.write(f)
        return pdf_path
    return _create_pdf


@pytest.mark.parametrize("pdf_properties", [
    {"size": (72, 72), "num_pages": 1},
    {"size": (72, 72), "num_pages": 2},
    {"size": (72, 72), "num_pages": 8},
    {"size": (144, 144), "num_pages": 2},
    {"size": (144, 144), "num_pages": 4},
])
def test_split(tmp_path, pdf_properties, create_pdf):
    pdf_file = create_pdf(size=pdf_properties["size"], num_pages=pdf_properties["num_pages"])
    output_dir = tmp_path / "_output"
    output_dir.mkdir()

    split_pdf(tmp_path, output_dir)

    output_files = os.listdir(output_dir)
    assert len(output_files) > 0, "No files were created in the output directory"

    for output_file in output_files:
        assert output_file.endswith('.pdf'), f"Unexpected file type found: {output_file}"
