################################################################################
#Analysis of keywords and most frequently occuring words in publications
#This is the function for analysis metric #1. Most frequently occuring words
#within a year.
#
#Sean Mackay
#8/19/2019
################################################################################
from os import listdir
from os.path import isfile, join
import sys
import os

#generates list of files
def genFileList(path):
    filesList=[]
    contents=os.listdir(path)
    for i in contents:
        if (i.endswith(".txt")):
            filesList.append(i)
            print(i)
    return filesList

#return file contents as data struct
def fileOpen(i):
    fileLinesList=[]
    filereader=open(i,'r')
    for line in filereader:
        fileLinesList.append(filereader.readline(line))
        print(line)
    return fileLinesList

#processes raw lines into usable data
def processLines(linesList):
    papersList=[]
    for i in linesList:
        if "FILENAME" in i:
            papersList.append(i[87,len(str)])
            papersList.append(i[82,86])
        else:
            papersList.append(i)



#most frequently occuring words by year
#def mostFrequentByYear():

#most frequently occuring words for a publication ever
#def mostFrequentOverall():

#will call appropriate file openers and other functions
def main (directory):
    filesList=genFileList(directory)

    for i in filesList:
        linesList=fileOpen(i)
        papersList=processLines(linesList)


if "__name__==__main__":
    directory= str(sys.path[0])
    directory=directory+"\Data"
    print(directory)
    main(directory)
