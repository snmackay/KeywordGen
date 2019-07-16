import subprocess
import sys
import PyPDF2
import textract
import operator
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
        if j in wordsFreq:
            wordsFreq[i]+=1
        else:
            wordsFreq[i]=1

    sorted_k = sorted(wordsFreq.items(), key=operator.itemgetter(1))
    correctList=sorted_k.reverse()
    top20=correctList[:20]

    return top20

def main(directory):
    install()
    files=genFileList(directory)

    pdfs={}
    for i in files:
        tokens=processFile(i)
        keywords=processText(tokens)
        pdfs[i]=generateKeywords(keywords)
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
