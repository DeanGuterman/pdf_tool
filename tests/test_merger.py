# import os
# import pytest
# import sys
# from pypdf import PdfWriter
#
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#
# from merger import merge_pdfs
#
# @pytest.fixture
# def setup_files(tmp_path):
#     test_files = []
#     for i in range(2):
#         test_pdf = tmp_path / f"test_{i}.pdf"
#         writer = PdfWriter()
#         writer.add_blank_page(width=72, height=72)
#         test_files.append(test_pdf)
#         with open(test_pdf, "wb") as f:
#             writer.write(f)
#     return test_files
#
#
# def test_merge(tmp_path):
#     output_dir = tmp_path / "output"
#     output_dir.mkdir()
#
#     output_file = merge_pdfs(tmp_path, output_dir)
#
#     assert output_file.endswith('.pdf'), f"Unexpected file type found: {output_file}"
