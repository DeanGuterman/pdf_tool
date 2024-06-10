import os
from PyPDF2 import PdfMerger
from utils import clear_folder


def merge_pdfs(input_folder, output_folder):
    """
    Merge multiple pdfs into a new singular pdf
    :param input_folder: The folder containing the pdfs to be merged
    :param output_folder: The folder that should hold the newly created pdf
    """

    # Clear the output folder
    clear_folder(output_folder)

    # Iterate through the pdfs in the input folder, while merging them into a merger
    merger = PdfMerger()
    for item in os.listdir(input_folder):
        if item.endswith('.pdf'):
            merger.append(os.path.join(input_folder, item))
            print(f"File {item} merged")
    output_file_path = os.path.join(output_folder, 'merged.pdf')
    # Write the merger into the resulting pdf
    merger.write(output_file_path)
    merger.close()
