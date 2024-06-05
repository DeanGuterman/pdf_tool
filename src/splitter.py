import PyPDF2
import os


def split_pdf(input_pdf, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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

if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser(description='Split a pdf into individual pages')
    parser.add_argument('input_pdf', help='Path to the input PDF file.')
    parser.add_argument('output_folder', help='Folder to save the split PDF pages')

    args = parser.parse_args()
    split_pdf(args.input_pdf, args.output_folder)
