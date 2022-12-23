from sys import argv
from PyPDF2 import PdfWriter

pdf_list = argv[1:]

def merge(pdf_list):
    '''
    merge pdf files
    '''
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged.pdf")
    merger.close()

merge(pdf_list)