import PyPDF2
import os


def split_pdf(input_pdf, output_folder):
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)

        for page_num in range(num_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])

            output_pdf_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
            with open(output_pdf_path, "wb") as output_pdf:
                writer.write(output_pdf)

            print(f"Page {page_num + 1} saved as {output_folder}")