import PyPDF2
#function to take text from file and return as string
def extractFromPDF(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfFilereader(pdf, strict=False)#False will continue to run even if errors encountered
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text


    if __name__ == '__main__':
        extracted_text = extractFromPDF('sample.pdf')
        coffee_count = 0
        #Iterates through and prints text to console
        for text in extracted_text:
            print(text)
