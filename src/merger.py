import os
from PyPDF2 import PdfMerger


def merge_pdfs(input_folder, output_folder):
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    merger = PdfMerger()
    for item in os.listdir(input_folder):
        if item.endswith('.pdf'):
            merger.append(os.path.join(input_folder, item))
            print(f"File {item} merged")
    output_file_path = os.path.join(output_folder, 'merged.pdf')
    merger.write(output_file_path)
    merger.close()
