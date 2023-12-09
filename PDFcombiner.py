import PyPDF2
import os

pdfFiles = []
pdfDirectory = input("PDF directory")
directory = pdfDirectory
os.chdir(directory)

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)

for file in pdfFiles:
    print(f'\t{file}')

pdfWriter = PyPDF2.PdfWriter()
pdfFiles = sorted(pdfFiles, key=str.lower)

for filename in pdfFiles:
    pdfReader = PyPDF2.PdfReader(filename)
    for pageNum in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)


finalFile_name = input(str("What do you want to name your PDF file?: "))
finalFile_name += ".pdf"

pdfOutput = open(finalFile_name, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
