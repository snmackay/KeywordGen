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
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(directory)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(directory, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + genFileList(fullPath)
        elif fullPath.endswith(".pdf"):
            allFiles.append(fullPath)
    return allFiles

def processFile(fileName): #processes text into a readable stream
    fp = open(fileName, 'rb')
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
    return tokens

def findKeyword(keywords,stringy): #finds the first 30 words after the first occurance of "keywords"


    open('temp.txt', 'w').close()
    with open("temp.txt","a") as file1:
        for i in keywords:
                file1.write(i)
                file1.write('\n')

        file1.close()

    with open("temp.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    f.close()
    print(stringy)
    if stringy=="cse":
        counter=0
        for j in content:
            #print(type(j))
            if j=="keywords":
                ind_pos=[]
                for k in range(counter,counter+30):
                    ind_pos.append(content[k])
                combo="".join(ind_pos)
                combo=combo.split(";")
                returner=[]
                for k in combo:
                    returner.append(k)
                    combo.remove(k)

                return returner

            elif j=="keyword":
                ind_pos=[]
                for k in range(counter,counter+30):
                    ind_pos.append(content[k])
                combo="".join(ind_pos)
                combo=combo.split(";")
                returner=[]
                for k in combo:
                    returner.append(k)
                    combo.remove(k)
                return returner

            elif j=="keywords:":
                ind_pos=[]
                for k in range(counter,counter+30):
                    ind_pos.append(content[k])
                combo="".join(ind_pos)
                combo=combo.split(";")
                returner=[]
                for k in combo:
                    returner.append(k)
                    combo.remove(k)
                return returner
            counter+=1
    else:
        counter=0
        for j in content:
            #print(type(j))
            if j=="keywords":
                ind_pos=[]
                for k in range(counter,counter+30):
                    ind_pos.append(content[k])
                return ind_pos

            elif j=="keyword":
                ind_pos=[]
                for k in range(counter,counter+30):
                    ind_pos.append(content[k])
                return ind_pos

            elif j=="keywords:":
                ind_pos=[]
                for k in range(counter,counter+30):
                    ind_pos.append(content[k])
                return ind_pos
            counter+=1

def main(directory): #control/print function
    files=genFileList(directory)
    open('ProvidedKeywords.txt', 'w').close()

    pdfs={}
    for i in files:
        tokens=processFile(i)
        keywords=processText(tokens)
        #no switch statement native so here are cases for paper types
        if("/CSE/" in i):
            pdfs[i]=findKeyword(keywords,"cse")
        elif("/EDUCON/" in i):
            pdfs[i]=findKeyword(keywords,"educon")
        elif("/FIE/" in i):
            pdfs[i]=findKeyword(keywords,"fie")
        elif("/ICER/" in i):
            pdfs[i]=findKeyword(keywords,"icer")
        elif("/ITiCSE/" in i):
            pdfs[i]=findKeyword(keywords,"iticse")
        elif("/JECR/" in i):
            pdfs[i]=findKeyword(keywords,"jecr")
        elif("/Koli/" in i):
            pdfs[i]=findKeyword(keywords,"koli")
        elif("/SIGCSE/" in i):
            pdfs[i]=findKeyword(keywords,"sigcse")
        elif("/TOCE/" in i):
            pdfs[i]=findKeyword(keywords,"toce")
        elif("/TOE/" in i):
            pdfs[i]=findKeyword(keywords,"toe")
        elif("/WiPCSE/" in i):
            pdfs[i]=findKeyword(keywords,"wipcse")
        else:
            pdfs[i]=findKeyword(keywords,"none")
        print("Done "+i)

        with open("ProvidedKeywords.txt","a") as file1:
            for j in pdfs:
                if pdfs[j]!=None:
                    file1.write("FILENAME: "+j)
                    for item in pdfs[j]:
                        file1.write("%s\n" % item)

        file1.close()
    return 69

if "__name__==__main__":
    directory= str(sys.path[0])
    directory=directory+"/papers"
    main(directory)
