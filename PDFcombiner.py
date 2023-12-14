import PyPDF2
import os

pdfFiles = {}
pdfDirectory = input("PDF directory ")
directory = pdfDirectory
os.chdir(directory)

counter = 1
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdfFiles[counter] = filename
        counter += 1

for counter, file in pdfFiles.items():
    print(f'\t{counter}: {file}')

pdfWriter = PyPDF2.PdfWriter()

chosenFiles = []
print(f"Choose which files you want combined")
print(f"If all of them type 'all'. If you are finished, press 0")
while True:
    inputChoice = input(f'Please Choose file or an option: ')
    if inputChoice == "0":
        break
    elif inputChoice == "all":
        chosenFiles = list(pdfFiles.values())  # directly assign all values
        break
    else:
        try:
            choice = int(inputChoice)
            if choice in pdfFiles:  # Check if choice is a key in pdfFiles
                chosenFiles.append(pdfFiles[choice])
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

for filename in chosenFiles:
    pdfReader = PyPDF2.PdfReader(filename)
    for pageNum in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)


finalFile_name = input(str("What do you want to name your PDF file?: "))
finalFile_name += ".pdf"

pdfOutput = open(finalFile_name, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
