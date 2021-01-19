import PyPDF2
import sys

input = sys.argv[1:]

def pdf_combiner(pdfList):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfList:
        print(pdf)
        merger.append(pdf)

    merger.write('merged.pdf')


pdf_combiner(input)