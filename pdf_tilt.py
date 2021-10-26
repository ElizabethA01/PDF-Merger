
import PyPDF2

with open('dummy.pdf', 'rb') as file: # 'rb' reads the file in binary mode
    reader = PyPDF2.PdfFileReader(file) #another way of reading the file using PyPDF2 module
    # print(reader.numPages) #tells you number of pages

    #How to rotate PDFs to a new file:
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
