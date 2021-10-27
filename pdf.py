import PyPDF2
import sys

inputs = sys.argv[1:]
watermark_file = 'wtr.pdf'
output = 'super.pdf'
merged = 'watermarked-output.pdf'

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() #merge pages in the file
    for pdf in pdf_list:
        merger.append(pdf) #add pages
    #creates a new document
    merger.write(output) #created new documents


def watermarker(combined_file, watermarker):
    with open(combined_file, 'rb') as input_file, open(watermarker, 'rb') as watermark_file:
        #read content of the combined file
        input_pdf = PyPDF2.PdfFileReader(input_file)     
        #read content of the watermark
        watermark_pdf = PyPDF2.PdfFileReader(watermark_file)        
        #create a pdf writer object for the output file
        output_file = PyPDF2.PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            #get pages of the combined file
            combined_pages = input_pdf.getPage(i)

            #merge the two pages
            combined_pages.mergePage(watermark_pdf.getPage(0))

            #add page
            output_file.addPage(combined_pages)
            print(combined_pages)
            print(output_file)

            with open(merged, 'wb') as merged_file:
                #write the watermarked file to the new file 
                output_file.write(merged_file)


pdf_combiner(inputs)
watermarker(output, watermark_file)


