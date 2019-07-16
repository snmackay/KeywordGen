import subprocess
import sys
import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Installs required packages
def install():
    subprocess.call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    subprocess.call([sys.executable, "-m", "pip", "install", "textract"])
    subprocess.call([sys.executable, "-m", "pip", "install", "nltk"])

def genFileList():
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            # print(os.path.join(directory, filename))
            files.append(filename)
        else:
            continue

    return files

def processFile(fileName):
    pdfFileObj = open(fileName,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    num_pages = pdfReader.numPages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
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
    keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
    return keywords

def generateKeyWords(keywords):
    wordsFreq={}

    for i in keywords:
        if i in wordsFreq:
            wordsFreq[i]+=1
        else:
            wordsFreq[i]=1

    return wordsFreq

def main(directory):
    install()
    files=genFileList(directory)

    pdfs={}
    for i in files:
        tokens=processFile(i)
        keywords=processText(tokens)
        pdfs[i]=generateKeywords(keywords)
        print("Done "+i)

    for j in pdfs:
        for k in pdfs[j]
        





if "__name__==__main__":
    directory= str(sys.argv[1])
    main(directory)
