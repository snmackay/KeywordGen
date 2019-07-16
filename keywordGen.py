import subprocess
import sys
import os
import PyPDF2
import textract
import operator
from os import listdir
from os.path import isfile, join
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


def genFileList(directory):
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            # print(os.path.join(directory, filename))
            files.append(filename)
        else:
            continue

    return files

def processFile(fileName):

    fileReader = PyPDF2.PdfFileReader(open(directory+"/"+fileName,'rb'))

    num_pages = fileReader.numPages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = fileReader.getPage(count)
        count +=1
        text += pageObj.extractText()

    if text != "":
        text = text

    else:
        text = textract.process(fileurl, method='tesseract', language='eng')

    tokens = word_tokenize(text)
    return tokens

def processText(fileText):
    punctuations = ['(',')',';',':','[',']',',']
    stop_words = stopwords.words('english')
    keywords = [word for word in fileText if not word in stop_words and not word in punctuations]
    return keywords

def generateKeyWords(keywords):
    wordsFreq={}

    for i in keywords:
        if i in wordsFreq:
            wordsFreq[i]+=1
        else:
            wordsFreq[i]=1

    sorted_k = sorted(wordsFreq.items(), key=operator.itemgetter(1))
    correctList=sorted_k.reverse()
    top20=correctList[:20]

    return top20

def main(directory):
    files=genFileList(directory)

    pdfs={}
    for i in files:
        tokens=processFile(i)
        keywords=processText(tokens)
        pdfs[i]=generateKeyWords(keywords)
        print("Done "+i)

    file1 = open("KeywordsForPapers.txt","a")

    for j in pdfs:
        file1.writeline(" ")
        file1.write(j)
        file1.writelines(pdfs[j])
        file1.writeline(" ")

    file1.close()
    return 69


if "__name__==__main__":
    directory= str(sys.argv[1])
    main(directory)
