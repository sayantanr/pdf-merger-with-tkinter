#!/usr/bin/python3
# geektechstuff

# libraries to import
from tkinter import *
from tkinter import filedialog
import PyPDF2

# defining variables
pdf2merge=[]
pdfWriter = PyPDF2.PdfFileWriter()

# creates Tk window
root = Tk()
root.update()
root.withdraw()

# asks user how many PDFs to merge
number_to_merge = input('How may files to merge?: ')
number_to_merge = int(number_to_merge)

# asks users where the PDFs are
for x in range(number_to_merge):
    pdf_to_merge = filedialog.askopenfilename()
    root.withdraw()
    root.update()
    pdf2merge.append(pdf_to_merge)

# Ask user for the name to save the file as
userfilename = filedialog.asksaveasfilename()

# loop through all PDFs
for filename in pdf2merge:
    # rb for read binary
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
# save PDF to file, wb for write binary
pdfOutput = open(userfilename + '.pdf', 'wb')
# Outputting the PDF
pdfWriter.write(pdfOutput)
# Closing the PDF writer
pdfOutput.close()
# closes Tk window
root.destroy()

print('Finished')
