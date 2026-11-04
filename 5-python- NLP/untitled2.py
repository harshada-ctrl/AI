# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:32:51 2026

@author: Admin
"""
#from PyPDF2 import PdfFi1eReader
# importin re uired modules
from PyPDF2 import PdfReader

#creating a pdf reader object

reader = PdfReader('c:/5-python- NLP/python_tutorial.pdf')


#printing number of pages in pdf file
print(len(reader.pages))

#getting a specific page from the pdf file
page = reader.pages[10]

