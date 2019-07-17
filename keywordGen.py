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

def genFileList(directory):
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            files.append(filename)
        else:
            continue
    return files

def processFile(fileName):
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

def processText(textblock):
    tokens=textblock.split(" ")
    tokens = [w.lower() for w in tokens]
    tooShort=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    stop_words = stopwords.words('english')
    keywords = [word for word in tokens if not word in stop_words and not word in tooShort]
    keywords = [word for word in keywords if word.isalpha()]
    return keywords

def generateKeyWords(keywords):
    wordsFreq={}

    for i in keywords:
        if i in wordsFreq:
            wordsFreq[i]+=1
        else:
            wordsFreq[i]=1

    sorted_k = sorted(wordsFreq.items(), key=operator.itemgetter(1))
    top30=sorted_k[-30:]

    return top30

def getProvidedWords(tokens):
    tokens=textblock.split(" ")
    tokens = [w.lower() for w in tokens]

def main(directory):
    files=genFileList(directory)
    open('Keywords.txt', 'w').close()

    pdfs={}
    for i in files:
        tokens=processFile(i)
        keywords=processText(tokens)
        pdfs[i]=generateKeyWords(keywords)
        print("Done "+i)

    with open("Keywords.txt","a") as file1:
        for j in pdfs:
            file1.write("FILENAME: "+j)
            file1.write('\n')
            file1.write('\n'.join('%s %s' % x for x in pdfs[j]))
            file1.write('\n')
            file1.write('\n')

    file1.close()
    return 69

if "__name__==__main__":
    directory= str(sys.argv[1])
    main(directory)
