#-*. coding: utf-8 -*-
#author: David Quesada López

from pylatex import Document, Section, Subsection, Tabular, MultiColumn, MultiRow, Figure
from PIL import Image
import os

def pdfTable(header, videos):
	imgName = 'tmp.png'
	
	doc = Document(header[4])
	section = Section(header[4])
	#header[3].save(imgName)
	image_filename = os.path.join(os.path.dirname(__file__), imgName)
	
	table1 = Tabular('|c|c|c|c|')
	table1.add_hline()
	table1.add_row((MultiColumn(4, align='|c|', data='Multicolumn'),))
	table1.add_hline()
	table1.add_row((doc.create(Figure(position='h!')).add_image(image_filename, width='246px'), 2, 3, 4))


h = [0,0,0,0,'Test header']
v = []

pdfTable(h,v)
