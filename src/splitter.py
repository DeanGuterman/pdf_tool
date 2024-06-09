import PyPDF2
import os


def split_pdf(input_pdf, output_folder):
    """
    Splits a pdf into multiple pdfs, each containing one page
    :param input_pdf: The file to be split
    :param output_folder: The folder that should hold the new pdfs
    """
    # Clear the output folder
    # TODO: CLEAN CODE THE REPEATS IN MERGER.PY
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Open the input pdf
    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)

        # Iterate through the input pdf and write each page to a new, separate pdf
        for page_num in range(num_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])

            output_pdf_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
            with open(output_pdf_path, "wb") as output_pdf:
                writer.write(output_pdf)

            print(f"Page {page_num + 1} saved as {output_folder}")