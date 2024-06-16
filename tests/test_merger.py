import os
import pytest
import sys
from pypdf import PdfWriter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from merger import merge_pdfs


@pytest.fixture
def create_test_pdfs(tmp_path):
    def _create_test_pdfs(num_files=5, page_size=(72, 72)):
        test_files = []
        for i in range(num_files):
            test_pdf = tmp_path / f"test_{i}.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=page_size[0], height=page_size[1])
            with open(test_pdf, "wb") as f:
                writer.write(f)
            test_files.append(test_pdf)
        return test_files
    return _create_test_pdfs


@pytest.mark.parametrize("pdf_properties", [
    {"num_files": 3, "page_size": (72, 72)},
    {"num_files": 5, "page_size": (72, 72)},
    {"num_files": 2, "page_size": (144, 144)},
    {"num_files": 7, "page_size": (144, 144)},
])
def test_merge(tmp_path, pdf_properties, create_test_pdfs):
    create_test_pdfs(num_files=pdf_properties["num_files"], page_size=pdf_properties["page_size"])
    output_dir = tmp_path / "_output"
    output_dir.mkdir()

    merge_pdfs(tmp_path, output_dir)
    output_files = os.listdir(output_dir)

    assert len(os.listdir(output_dir)) > 0, "No files were created in the output directory"
    assert all(file.endswith('.pdf') for file in output_files), f"Unexpected file type found: {output_files}"

