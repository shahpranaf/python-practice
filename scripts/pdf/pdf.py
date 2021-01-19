import PyPDF2

with open('dummy.pdf', 'rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader)        
    print(reader.numPages)        
    
    page = reader.getPage(0)

    rotatePdf = page.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(rotatePdf);
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)