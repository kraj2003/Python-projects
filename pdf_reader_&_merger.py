from pypdf import PdfReader,PdfMerger
import os
#pdfreader
reader=PdfReader("the_silent_patient.pdf")
no_of_pages=len(reader.pages)
page=reader.pages[0]
text=page.extract_text()
print(reader)
print(no_of_pages)
print(page)
print(text)

#pdfmerger
a=0  
merge=PdfMerger()
for x in os.listdir():
    if x.endswith(".pdf"):
        print(x)
        readr=PdfReader(x)
        pags=len(readr.pages)
        print(pags)
        # merger=PdfFileMerger(x)
        merge.append(x)
        print(merge)
merge.write("mergedpdf.pdf")
merge.close()