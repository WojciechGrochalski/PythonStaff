import PyPDF2
from fpdf import FPDF
import textwrap

pdf_file = open('C:/Users/alche/OneDrive/Pulpit/l2.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
pdf_file.close()

x=textwrap.dedent(page_content)
#MyTxt=open('C:/Users/alche/OneDrive/Pulpit/mypdf.pdf', 'w')

width=110
txt1=(textwrap.fill(x, width=width))
line=1
lnt=1
pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 13.0)

pdf.write(8, txt=txt1)
 #pdf.cell(500,8,ln=i, align='C',  txt=txt.format(line), border=0)
 #line+=1

pdf.output('test1.pdf', 'F')


