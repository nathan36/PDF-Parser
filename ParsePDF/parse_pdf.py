from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

str = convert('Daily Traffic Statistics for Pattullo Bridge - June 6 2018.pdf', pages=[0])

# split str by '\n'
#text_array = str.split("\n")
#word_array = []
#for item in text_array:
#    word_array.append(item.split(","))

with open('pdf.txt', 'wb') as file:
    file.write(str)
file.close()
