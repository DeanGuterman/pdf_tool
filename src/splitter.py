import os
from pypdf import PdfReader, PdfWriter
from utils import clear_folder


def split_pdf(input_folder, output_folder):
    """
    Splits a pdf into multiple pdfs, each containing one page
    :param input_folder: The folder that hold the file to be split
    :param output_folder: The folder that should hold the new pdfs
    :return: The output folder's path
    """

    # Clear the output folder
    clear_folder(output_folder)

    input_pdf = os.path.join(input_folder, os.listdir(input_folder)[0])
    # Open the input pdf
    with open(input_pdf, "rb") as pdf_file:
        reader = PdfReader(pdf_file)

        # Iterate through the input pdf and write each page to a new, separate pdf
        for page_num in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            output_pdf_path = os.path.join(output_folder, f"{os.path.basename(input_pdf).split('.')[0]}_page_{page_num + 1}.pdf")
            with open(output_pdf_path, "wb") as output_pdf:
                writer.write(output_pdf)

    clear_folder(input_folder)
    return output_folder
