import os
from pypdf import PdfWriter
from utils import clear_folder


def merge_pdfs(input_folder, output_folder):
    """
    Merge multiple pdfs into a new singular pdf
    :param input_folder: The folder containing the pdfs to be merged
    :param output_folder: The folder that should hold the newly created pdf
    :return: The newly created file's path
    """

    # Clear the output folder
    clear_folder(output_folder)
    # Iterate through the pdfs in the input folder, while writing them into a single file
    writer = PdfWriter()
    for item in os.listdir(input_folder):
        if item.endswith('.pdf'):
            writer.append(os.path.join(input_folder, item))
            print(f"File {item} merged")
    output_file_path = os.path.join(output_folder, 'merged.pdf')
    # Write the merger into the resulting pdf
    writer.write(output_file_path)
    writer.close()
    clear_folder(input_folder)
    return output_file_path
