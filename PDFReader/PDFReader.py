import pyPDF2

def extractFromPDF(pdf_file: str) -> [str]:
    with open(pdf_file)