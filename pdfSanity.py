#this is a combination of earlier applications keywordGen.py and keywordGrabber.py

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
        elif fullPath.endswith(".pdf") and fullPath not in allFiles:
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
        #print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                textblock+=text
    return textblock

#processes text for finding provided Keywords
def processText(textblock): #removes garbage text
    tokens=textblock.split(" ")
    tokens = [w.lower() for w in tokens]
    return tokens

#processes text for finding most frequent words
def processText2(textblock):
    tokens=textblock.split(" ")
    tokens = [w.lower() for w in tokens]
    tooShort=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    stop_words = stopwords.words('english')
    keywords = [word for word in tokens if not word in stop_words and not word in tooShort]
    keywords = [word for word in keywords if word.isalpha()]
    return keywords

def generateTrueKeyWords(keywords):
    wordsFreq={}

    for i in keywords:
        if i in wordsFreq:
            wordsFreq[i]+=1
        else:
            wordsFreq[i]=1

    sorted_k = sorted(wordsFreq.items(), key=operator.itemgetter(1))
    top30=sorted_k[-30:] #[:30]

    return top30


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
    if stringy=="educon":
        counter=0
        for j in content:

            if "keywords" in j or "keyword" in j or "keywords:" in j:
                ind_pos=[]
                for k in range(counter,counter+30):
                    ind_pos.append(content[k])

                combo=" ".join(ind_pos)
                combo=combo.split("i.")
                if(";" in combo[0]):
                    combo=combo[0].split("; ")
                else:
                    combo=combo[0].split(", ")
                returner=[]
                for k in combo:
                    returner.append(k)
                temper=returner[0]
                temper[:8]
                returner[0]=temper
                return returner
            counter+=1


def main(directory): #control/print function
    files=genFileList(directory)
    open('ProvidedKeywords.txt', 'w').close()

    pdfs={}
    pdfs2={}
    for i in files:
        tokens=processFile(i)
        keywords=processText(tokens)
        keywords2=processText2(tokens)
        #no switch statement native so here are cases for paper types
        fileName=""
        fileName2=""
        if("/CSE/" in i):
            pdfs[i]=findKeyword(keywords,"cse")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="CSE.txt"
            fileName2="CSEActual.txt"
        elif("/EDUCON/" in i):
            pdfs[i]=findKeyword(keywords,"educon")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="educon.txt"
            fileName2="educonActual.txt"
        elif("/FIE/" in i):
            pdfs[i]=findKeyword(keywords,"educon")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="fie.txt"
            fileName2="fieActual.txt"
        elif("/ICER/" in i):
            pdfs[i]=findKeyword(keywords,"icer")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="icer.txt"
            fileName2="icerActual.txt"
        elif("/ITiCSE/" in i):
            pdfs[i]=findKeyword(keywords,"iticse")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="iticse.txt"
            fileName2="iticseActual.txt"
        elif("/JECR/" in i):
            pdfs[i]=findKeyword(keywords,"jecr")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="jecr.txt"
            fileName2="jecrActual.txt"
        elif("/Koli/" in i):
            pdfs[i]=findKeyword(keywords,"koli")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="koli.txt"
            fileName2="koliActual.txt"
        elif("/SIGCSE/" in i):
            pdfs[i]=findKeyword(keywords,"sigcse")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="sigcse.txt"
            fileName2="sigcseActual.txt"
        elif("/TOCE/" in i):
            pdfs[i]=findKeyword(keywords,"toce")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="toce.txt"
            fileName2="toceActual.txt"
        elif("/TOE/" in i):
            pdfs[i]=findKeyword(keywords,"toe")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="toe.txt"
            fileName2="toeActual.txt"
        elif("/WiPCSE/" in i):
            pdfs[i]=findKeyword(keywords,"wipcse")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="wipcse.txt"
            fileName2="wipcseActual.txt"
        else:
            pdfs[i]=findKeyword(keywords,"none")
            pdfs2[i]=generateTrueKeyWords(keywords2)
            fileName="other.txt"
            fileName2="otherActual.txt"

        print("Done "+i)

    with open(fileName,"a") as file1:
        for j in pdfs:
            if pdfs[j]!=None:
                file1.write("FILENAME: "+j+"\n")
                for item in pdfs[j]:
                    file1.write("    "+"%s\n" % item )
                file1.write("\n")

    file1.close()

    with open(fileName2,"a") as file2:
        for j in pdfs:
            file2.write("FILENAME: "+j)
            file2.write('\n')
            file2.write('\n'.join('%s %s' % x for x in pdfs2[j]))
            file2.write('\n')
            file2.write('\n')

    file2.close()
    return 69

if "__name__==__main__":
    directory= str(sys.path[0])
    directory=directory+"/papers"
    main(directory)
