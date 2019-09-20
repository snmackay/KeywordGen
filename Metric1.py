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

#helper function for mostFrequentByYear that seperates word from frequency and returns a tuple
def seperator(pair):
    return pair.split(" ")

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

    words2018={}
    words2017={}
    words2016={}
    words2015={}
    words2014={}
    words2013={}
    words2012={}
    words2011={}
    words2010={}
    words2009={}
    words2008={}
    words2007={}

    counter=0
    for i in contents:
        tempTuple=()
        if "2018" in i:
            common2018.append(contents[counter]+ "  :  "+contents[counter+30])
            common2018.append(contents[counter]+ "  :  "+contents[counter+29])
            common2018.append(contents[counter]+ "  :  "+contents[counter+28])
            common2018.append(contents[counter]+ "  :  "+contents[counter+27])
            common2018.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2018:
                words2018[pair1[0]]=pair1[1]
                words2018[pair2[0]]=pair2[1]
                words2018[pair3[0]]=pair3[1]
                words2018[pair4[0]]=pair4[1]
                words2018[pair5[0]]=pair5[1]
            else:
                words2018[pair1[0]]+=pair1[1]
                words2018[pair2[0]]+=pair2[1]
                words2018[pair3[0]]+=pair3[1]
                words2018[pair4[0]]+=pair4[1]
                words2018[pair5[0]]+=pair5[1]

        elif "2017" in i:
            common2017.append(contents[counter]+ "  :  "+contents[counter+30])
            common2017.append(contents[counter]+ "  :  "+contents[counter+29])
            common2017.append(contents[counter]+ "  :  "+contents[counter+28])
            common2017.append(contents[counter]+ "  :  "+contents[counter+27])
            common2017.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2017:
                words2017[pair1[0]]=pair1[1]
                words2017[pair2[0]]=pair2[1]
                words2017[pair3[0]]=pair3[1]
                words2017[pair4[0]]=pair4[1]
                words2017[pair5[0]]=pair5[1]
            else:
                words2017[pair1[0]]+=pair1[1]
                words2017[pair2[0]]+=pair2[1]
                words2017[pair3[0]]+=pair3[1]
                words2017[pair4[0]]+=pair4[1]
                words2017[pair5[0]]+=pair5[1]


        elif "2016" in i:
            common2016.append(contents[counter]+ "  :  "+contents[counter+30])
            common2016.append(contents[counter]+ "  :  "+contents[counter+29])
            common2016.append(contents[counter]+ "  :  "+contents[counter+28])
            common2016.append(contents[counter]+ "  :  "+contents[counter+27])
            common2016.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2016:
                words2016[pair1[0]]=pair1[1]
                words2016[pair2[0]]=pair2[1]
                words2016[pair3[0]]=pair3[1]
                words2016[pair4[0]]=pair4[1]
                words2016[pair5[0]]=pair5[1]
            else:
                words2016[pair1[0]]+=pair1[1]
                words2016[pair2[0]]+=pair2[1]
                words2016[pair3[0]]+=pair3[1]
                words2016[pair4[0]]+=pair4[1]
                words2016[pair5[0]]+=pair5[1]


        elif "2015" in i:
            common2015.append(contents[counter]+ "  :  "+contents[counter+30])
            common2015.append(contents[counter]+ "  :  "+contents[counter+29])
            common2015.append(contents[counter]+ "  :  "+contents[counter+28])
            common2015.append(contents[counter]+ "  :  "+contents[counter+27])
            common2015.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2015:
                words2015[pair1[0]]=pair1[1]
                words2015[pair2[0]]=pair2[1]
                words2015[pair3[0]]=pair3[1]
                words2015[pair4[0]]=pair4[1]
                words2015[pair5[0]]=pair5[1]
            else:
                words2015[pair1[0]]+=pair1[1]
                words2015[pair2[0]]+=pair2[1]
                words2015[pair3[0]]+=pair3[1]
                words2015[pair4[0]]+=pair4[1]
                words2015[pair5[0]]+=pair5[1]


        elif "2014" in i:
            common2014.append(contents[counter]+ "  :  "+contents[counter+30])
            common2014.append(contents[counter]+ "  :  "+contents[counter+29])
            common2014.append(contents[counter]+ "  :  "+contents[counter+28])
            common2014.append(contents[counter]+ "  :  "+contents[counter+27])
            common2014.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2014:
                words2014[pair1[0]]=pair1[1]
                words2014[pair2[0]]=pair2[1]
                words2014[pair3[0]]=pair3[1]
                words2014[pair4[0]]=pair4[1]
                words2014[pair5[0]]=pair5[1]
            else:
                words2014[pair1[0]]+=pair1[1]
                words2014[pair2[0]]+=pair2[1]
                words2014[pair3[0]]+=pair3[1]
                words2014[pair4[0]]+=pair4[1]
                words2014[pair5[0]]+=pair5[1]

        elif "2013" in i:
            common2013.append(contents[counter]+ "  :  "+contents[counter+30])
            common2013.append(contents[counter]+ "  :  "+contents[counter+29])
            common2013.append(contents[counter]+ "  :  "+contents[counter+28])
            common2013.append(contents[counter]+ "  :  "+contents[counter+27])
            common2013.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2013:
                words2013[pair1[0]]=pair1[1]
                words2013[pair2[0]]=pair2[1]
                words2013[pair3[0]]=pair3[1]
                words2013[pair4[0]]=pair4[1]
                words2013[pair5[0]]=pair5[1]
            else:
                words2013[pair1[0]]+=pair1[1]
                words2013[pair2[0]]+=pair2[1]
                words2013[pair3[0]]+=pair3[1]
                words2013[pair4[0]]+=pair4[1]
                words2013[pair5[0]]+=pair5[1]

        elif "2012" in i:
            common2012.append(contents[counter]+ "  :  "+contents[counter+30])
            common2012.append(contents[counter]+ "  :  "+contents[counter+29])
            common2012.append(contents[counter]+ "  :  "+contents[counter+28])
            common2012.append(contents[counter]+ "  :  "+contents[counter+27])
            common2012.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2012:
                words2012[pair1[0]]=pair1[1]
                words2012[pair2[0]]=pair2[1]
                words2012[pair3[0]]=pair3[1]
                words2012[pair4[0]]=pair4[1]
                words2012[pair5[0]]=pair5[1]
            else:
                words2012[pair1[0]]+=pair1[1]
                words2012[pair2[0]]+=pair2[1]
                words2012[pair3[0]]+=pair3[1]
                words2012[pair4[0]]+=pair4[1]
                words2012[pair5[0]]+=pair5[1]


        elif "2011" in i:
            common2011.append(contents[counter]+ "  :  "+contents[counter+30])
            common2011.append(contents[counter]+ "  :  "+contents[counter+29])
            common2011.append(contents[counter]+ "  :  "+contents[counter+28])
            common2011.append(contents[counter]+ "  :  "+contents[counter+27])
            common2011.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2011:
                words2011[pair1[0]]=pair1[1]
                words2011[pair2[0]]=pair2[1]
                words2011[pair3[0]]=pair3[1]
                words2011[pair4[0]]=pair4[1]
                words2011[pair5[0]]=pair5[1]
            else:
                words2011[pair1[0]]+=pair1[1]
                words2011[pair2[0]]+=pair2[1]
                words2011[pair3[0]]+=pair3[1]
                words2011[pair4[0]]+=pair4[1]
                words2011[pair5[0]]+=pair5[1]


        elif "2010" in i:
            common2010.append(contents[counter]+ "  :  "+contents[counter+30])
            common2010.append(contents[counter]+ "  :  "+contents[counter+29])
            common2010.append(contents[counter]+ "  :  "+contents[counter+28])
            common2010.append(contents[counter]+ "  :  "+contents[counter+27])
            common2010.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2010:
                words2010[pair1[0]]=pair1[1]
                words2010[pair2[0]]=pair2[1]
                words2010[pair3[0]]=pair3[1]
                words2010[pair4[0]]=pair4[1]
                words2010[pair5[0]]=pair5[1]
            else:
                words2010[pair1[0]]+=pair1[1]
                words2010[pair2[0]]+=pair2[1]
                words2010[pair3[0]]+=pair3[1]
                words2010[pair4[0]]+=pair4[1]
                words2010[pair5[0]]+=pair5[1]

        elif "2009" in i:
            common2009.append(contents[counter]+ "  :  "+contents[counter+30])
            common2009.append(contents[counter]+ "  :  "+contents[counter+29])
            common2009.append(contents[counter]+ "  :  "+contents[counter+28])
            common2009.append(contents[counter]+ "  :  "+contents[counter+27])
            common2009.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2009:
                words2009[pair1[0]]=pair1[1]
                words2009[pair2[0]]=pair2[1]
                words2009[pair3[0]]=pair3[1]
                words2009[pair4[0]]=pair4[1]
                words2009[pair5[0]]=pair5[1]
            else:
                words2009[pair1[0]]+=pair1[1]
                words2009[pair2[0]]+=pair2[1]
                words2009[pair3[0]]+=pair3[1]
                words2009[pair4[0]]+=pair4[1]
                words2009[pair5[0]]+=pair5[1]

        elif "2008" in i:
            common2008.append(contents[counter]+ "  :  "+contents[counter+30])
            common2008.append(contents[counter]+ "  :  "+contents[counter+29])
            common2008.append(contents[counter]+ "  :  "+contents[counter+28])
            common2008.append(contents[counter]+ "  :  "+contents[counter+27])
            common2008.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2008:
                words2008[pair1[0]]=pair1[1]
                words2008[pair2[0]]=pair2[1]
                words2008[pair3[0]]=pair3[1]
                words2008[pair4[0]]=pair4[1]
                words2008[pair5[0]]=pair5[1]
            else:
                words2008[pair1[0]]+=pair1[1]
                words2008[pair2[0]]+=pair2[1]
                words2008[pair3[0]]+=pair3[1]
                words2008[pair4[0]]+=pair4[1]
                words2008[pair5[0]]+=pair5[1]

        elif "2007" in i:
            common2007.append(contents[counter]+ "  :  "+contents[counter+30])
            common2007.append(contents[counter]+ "  :  "+contents[counter+29])
            common2007.append(contents[counter]+ "  :  "+contents[counter+28])
            common2007.append(contents[counter]+ "  :  "+contents[counter+27])
            common2007.append(contents[counter]+ "  :  "+contents[counter+26])

            pair1=seperator(contents[counter+30])
            pair2=seperator(contents[counter+30])
            pair3=seperator(contents[counter+30])
            pair4=seperator(contents[counter+30])
            pair5=seperator(contents[counter+30])

            if contents[counter+30] not in words2007:
                words2007[pair1[0]]=pair1[1]
                words2007[pair2[0]]=pair2[1]
                words2007[pair3[0]]=pair3[1]
                words2007[pair4[0]]=pair4[1]
                words2007[pair5[0]]=pair5[1]
            else:
                words2007[pair1[0]]+=pair1[1]
                words2007[pair2[0]]+=pair2[1]
                words2007[pair3[0]]+=pair3[1]
                words2007[pair4[0]]+=pair4[1]
                words2007[pair5[0]]+=pair5[1]

        counter+=1

    results={}
    results[2018]=common2018
    results[2017]=common2017
    results[2016]=common2016
    results[2015]=common2015
    results[2014]=common2014
    results[2013]=common2013
    results[2012]=common2012
    results[2011]=common2011
    results[2010]=common2010
    results[2009]=common2009
    results[2008]=common2008
    results[2007]=common2007

    results[18]=words2018
    results[17]=words2017
    results[16]=words2016
    results[15]=words2015
    results[14]=words2014
    results[13]=words2013
    results[12]=words2012
    results[11]=words2011
    results[10]=words2010
    results[9]=words2009
    results[8]=words2008
    results[7]=words2007
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
