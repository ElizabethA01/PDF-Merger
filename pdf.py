import PyPDF2
import sys

inputs = sys.argv[1:]
watermark_file = 'wtr.pdf'
output = 'superfile.pdf'

def pdf_combiner(pdf_list):
    #merge pages in the file
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        #add pages
        merger.append(pdf)
    #creates a new document
    merger.write(output)


def watermarker(combined_file, watermark_file):
    with open(combined_file, 'rb') as filehandle_input:
        #read content of the combined file
        pdf2 = PyPDF2.PdfFileReader(filehandle_input)

        with open(watermark_file, 'rb') as filehandle_watermark:
            #read content of the watermark
            watermark = PyPDF2.PdfFileReader(filehandle_watermark)

            for page in combined_file:

                #get pages of the combined file
                combined_pages = pdf2.getPage(page)

                #get first page of the watermark PDF
                first_page_watermark = watermark.getPage(0)

                #merge the two pages
                combined_pages.mergePage(first_page_watermark)

                #create a pdf writer object for the output file
                pdf_writer = PyPDF2.PdfFileWriter()

                #add page
                pdf_writer.addPage(combined_pages)

                with open('watermarked-super.pdf', 'wb') as filehandle_output:
                    #write the watermarked file to the new file 
                    pdf_writer.write(filehandle_output)


        


pdf_combiner(inputs)
watermarker(output, watermark_file)


