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

    path=sys.path[0]+"\\Data\\"+i
    filereader=open(path,encoding='utf-8')
    content = filereader.readlines()
    content = [x.strip() for x in content]
    return content

#processes raw lines into usable data
def processLines(linesList):
    papersList=[]
    for i in linesList:
        if "FILENAME" in i:
            papersList.append(i[87:len(i)])
            papersList.append(i[82:86])
        else:
            papersList.append(i)

    return papersList



#most frequently occuring words by year
def mostFrequentByYear(contents):

    #lists for each year
    common2018=[]
    common2017=[]
    common2016=[]
    common2015=[]
    common2014=[]
    common2013=[]
    common2012=[]
    common2011=[]
    common2010=[]
    common2009=[]
    common2008=[]
    common2007=[]

    counter=0
    for i in contents:
        tempTuple=()
        if "2018" in i:
            common2018.append(contents[counter]+ "  :  "+contents[counter+30])
            common2018.append(contents[counter]+ "  :  "+contents[counter+29])
            common2018.append(contents[counter]+ "  :  "+contents[counter+28])
            common2018.append(contents[counter]+ "  :  "+contents[counter+27])
            common2018.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2017" in i:
            common2017.append(contents[counter]+ "  :  "+contents[counter+30])
            common2017.append(contents[counter]+ "  :  "+contents[counter+29])
            common2017.append(contents[counter]+ "  :  "+contents[counter+28])
            common2017.append(contents[counter]+ "  :  "+contents[counter+27])
            common2017.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2016" in i:
            common2016.append(contents[counter]+ "  :  "+contents[counter+30])
            common2016.append(contents[counter]+ "  :  "+contents[counter+29])
            common2016.append(contents[counter]+ "  :  "+contents[counter+28])
            common2016.append(contents[counter]+ "  :  "+contents[counter+27])
            common2016.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2015" in i:
            common2015.append(contents[counter]+ "  :  "+contents[counter+30])
            common2015.append(contents[counter]+ "  :  "+contents[counter+29])
            common2015.append(contents[counter]+ "  :  "+contents[counter+28])
            common2015.append(contents[counter]+ "  :  "+contents[counter+27])
            common2015.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2014" in i:
            common2014.append(contents[counter]+ "  :  "+contents[counter+30])
            common2014.append(contents[counter]+ "  :  "+contents[counter+29])
            common2014.append(contents[counter]+ "  :  "+contents[counter+28])
            common2014.append(contents[counter]+ "  :  "+contents[counter+27])
            common2014.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2013" in i:
            common2013.append(contents[counter]+ "  :  "+contents[counter+30])
            common2013.append(contents[counter]+ "  :  "+contents[counter+29])
            common2013.append(contents[counter]+ "  :  "+contents[counter+28])
            common2013.append(contents[counter]+ "  :  "+contents[counter+27])
            common2013.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2012" in i:
            common2012.append(contents[counter]+ "  :  "+contents[counter+30])
            common2012.append(contents[counter]+ "  :  "+contents[counter+29])
            common2012.append(contents[counter]+ "  :  "+contents[counter+28])
            common2012.append(contents[counter]+ "  :  "+contents[counter+27])
            common2012.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2011" in i:
            common2011.append(contents[counter]+ "  :  "+contents[counter+30])
            common2011.append(contents[counter]+ "  :  "+contents[counter+29])
            common2011.append(contents[counter]+ "  :  "+contents[counter+28])
            common2011.append(contents[counter]+ "  :  "+contents[counter+27])
            common2011.append(contents[counter]+ "  :  "+contents[counter+26])

        elif "2010" in i:
            common2010.append(contents[counter]+ "  :  "+contents[counter+30])
            common2010.append(contents[counter]+ "  :  "+contents[counter+29])
            common2010.append(contents[counter]+ "  :  "+contents[counter+28])
            common2010.append(contents[counter]+ "  :  "+contents[counter+27])
            common2010.append(contents[counter]+ "  :  "+contents[counter+26])

        counter+=1

    results={}
    results[2018]=common2018
    results[2017]=common2017
    results[2016]=common2016
    return results






#most frequently occuring words for a publication ever
#def mostFrequentOverall():

#will call appropriate file openers and other functions
def main (directory):
    filesList=genFileList(directory)
    print(filesList)
    for i in filesList:
        if "Actual" in i:
            linesList=fileOpen(i)
            contents=processLines(linesList)

            print(i)
            results1=mostFrequentByYear(contents)

        elif "Actual" not in i:
            linesList=fileOpen(i)
            papersList=processLines(linesList)





if "__name__==__main__":
    directory= str(sys.path[0])
    directory=directory+"\Data"
    print(directory)
    main(directory)
