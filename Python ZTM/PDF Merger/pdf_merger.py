from sys import argv
from PyPDF2 import PdfWriter

pdf_list = argv[1:]

def merge(pdf_list):
    '''
    merge pdf files
    '''
    merger = PdfWriter()
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except:
            print("Ooops")
            print("Usage:   python .\pdf_merger.py pdf1.pdf pdf2.pdf")
            exit()

    merger.write("merged.pdf")
    merger.close()
    return None

merge(pdf_list)