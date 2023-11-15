import PyPDF2

def extractFromPDF(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfFilereader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text


    if __name__ == '__main__':
        extracted_text = extractFromPDF('file.pdf')
        for text in extracted_text:
            print(text)
