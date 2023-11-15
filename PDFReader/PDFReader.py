import pyPDF2

def extractFromPDF(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfFilereader(pdf, strict=False)
        pdf_text = []
