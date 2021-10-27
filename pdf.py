import PyPDF2
import sys

inputs = sys.argv[1:]
watermark_file = 'wtr.pdf'
output = 'super.pdf'
merged = 'watermakred-output.pdf'

def pdf_combiner(pdf_list):
    #merge pages in the file
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        #add pages
        merger.append(pdf)
    #creates a new document
    merger.write(output)


def watermarker(combined_file, watermarker):
    with open(combined_file, 'rb') as input_file, open(watermarker, 'rb') as watermark_file:
        #read content of the combined file
        input_pdf = PyPDF2.PdfFileReader(input_file)     
        #read content of the watermark
        watermark_pdf = PyPDF2.PdfFileReader(watermark_file)        
        #create a pdf writer object for the output file
        output = PyPDF2.PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            #get pages of the combined file
            combined_pages = input_pdf.getPage(i)

            #get first page of the watermark PDF
            watermark_page = watermark_pdf.getPage(0)

            #merge the two pages
            combined_pages.mergePage(watermark_page)

            #add page
            output.addPage(combined_pages)

            with open(merged, 'wb') as merged_file:
                #write the watermarked file to the new file 
                output.write(merged_file)


pdf_combiner(inputs)
watermarker(output, watermark_file)


