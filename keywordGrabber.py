import subprocess
import sys
import os
import textract
import operator
import itertools
from os import listdir
from os.path import isfile, join
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import numpy as np

def genFileList(directory): #creates the list of files to be parsed
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            files.append(filename)
        else:
            continue
    return files

def processFile(fileName): #processes text into a readable stream
    fp = open(directory+'/'+fileName, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    textblock=""
    for page in pages:
        print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                textblock+=text
    return textblock

def processText(textblock): #removes garbage text
    tokens=textblock.split(" ")
    tokens = [w.lower() for w in tokens]
    tooShort=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    stop_words = stopwords.words('english')
    keywords = [word for word in tokens if not word in stop_words and not word in tooShort]
    keywords = [word for word in keywords if word.isalpha()]
    return keywords

def findKeyword(keywords): #finds the first 30 words after the first occurance of "keywords"
    counter=0
    for i in keywords:
        if i=="keywords":
            ind_pos=[]
            for k in range(counter,counter+1):
                ind_pos.append(k)

            arr=keywords[ind_pos]
            return arr

        if i=="keyword":
            ind_pos=[]
            for k in range(counter,counter+1):
                ind_pos.append(k)

            arr=keywords[ind_pos]
            return arr

        if i=="keywords:":
            ind_pos=[]
            for k in range(counter,counter+1):
                ind_pos.append(k)

            arr=keywords[ind_pos]
            return arr

        else:
            counter+=1
            continue

def main(directory): #control/print function
    files=genFileList(directory)
    open('ProvidedKeywords.txt', 'w').close()

    pdfs={}
    for i in files:
        tokens=processFile(i)
        keywords=processText(tokens)
        pdfs[i]=findKeyword(keywords)
        print("Done "+i)

    if None not in pdfs.values():
        with open("ProvidedKeywords.txt","a") as file1:
            for j in pdfs:
                file1.write("FILENAME: "+j)
                file1.write('\n')
                file1.write('\n'.join('%s %s' % x for x in pdfs[j]))
                file1.write('\n')
                file1.write('\n')

        file1.close()
    return 69

if "__name__==__main__":
    directory= str(sys.path[0])
    directory=directory+"/papers"
    main(directory)
