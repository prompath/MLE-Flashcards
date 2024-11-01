from glob import glob
from os import mkdir
from os.path import abspath, isdir, basename, splitext

from PyPDF2 import PdfWriter, PdfReader

OUTPUT_PATH = abspath("./split/")

if not isdir(OUTPUT_PATH):
    mkdir(OUTPUT_PATH)

pdfs = glob(abspath("./*.pdf"))

for pdf in pdfs:
    filename = splitext(basename(pdf))[0]
    parent_path = abspath(OUTPUT_PATH + "/" + filename)
    if not isdir(parent_path):
        mkdir(parent_path)
    pdf_obj = PdfReader(open(pdf, "rb"))
    for i in range(len(pdf_obj.pages)):
        output = PdfWriter()
        output.add_page(pdf_obj.pages[i])
        with open(f"{parent_path}/{filename}-page{i+1}.pdf", "wb") as outputStream:
            output.write(outputStream)
