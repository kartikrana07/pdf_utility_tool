from PyPDF2 import PdfReader, PdfWriter

def extract_pages(pdf_path, start, end, output_file):
    reader = PdfReader(pdf_path)

    writer = PdfWriter()

    for page in range(start - 1, end):
        writer.add_page(reader.pages[page])

    with open(output_file, "wb") as file:
        writer.write(file)