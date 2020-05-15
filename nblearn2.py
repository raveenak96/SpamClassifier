import sys,os,glob
from collections import defaultdict
import json
import string,re

################### Testing enhancements ########################

def main(argv) :
    directory = argv[0]

    trainFiles = glob.glob(directory + '/**/ham/*.txt', recursive=True)
    trainFiles.extend(glob.glob(directory + '/**/spam/*.txt', recursive=True))

    #selecting only 10% of train files
    #hamFiles = glob.glob(directory + '/**/ham/*.txt', recursive=True)
    #spamFiles = glob.glob(directory + '/**/spam/*.txt', recursive=True)
    #numFiles = int(((len(hamFiles)+len(spamFiles))*.1)/2)
    #trainFiles = hamFiles[:numFiles]
    #trainFiles.extend(spamFiles[:numFiles])

    fullDict = {}
    fullDict = defaultdict(lambda:0,fullDict)
    spamDict = {}
    spamDict = defaultdict(lambda: 0, spamDict)
    hamDict = {}
    hamDict = defaultdict(lambda: 0, hamDict)
    numSpam=numHam=totalSpamWords=totalHamWords= 0
    for trainFile in trainFiles :
        file = open(trainFile, "r", encoding="latin1")
        content = file.read().strip('/n').split()
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in content if len(w.translate(table)) > 0 ]
        if 'ham' in trainFile :
            numHam += 1
        else :
            numSpam += 1
        for word in stripped :
            word = word.lower()
            fullDict[word] += 1
            if 'ham' in trainFile :
                hamDict[word] += 1
                totalHamWords += 1
            else :
                spamDict[word] += 1
                totalSpamWords += 1
        file.close()
    vocabSize = len(fullDict)
    totalFiles = len(trainFiles)
    pSpam = numSpam/totalFiles
    pHam = numHam/totalFiles

    for word,_ in fullDict.items() :
        spamDict[word] = (spamDict[word] + .5) / (totalSpamWords + .5*vocabSize)
        hamDict[word] = (hamDict[word] + .5) / (totalHamWords + .5*vocabSize)

    outputFile = open('nbmodel.txt','w')
    outputFile.write(str(pSpam))
    outputFile.write('\n'+str(pHam)+'\n')
    outputFile.write(json.dumps(spamDict)+'\n')
    outputFile.write(json.dumps(hamDict))
    outputFile.close()

if __name__== "__main__" :
    main(sys.argv[1:])