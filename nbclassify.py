import sys,os,glob,json,math
import string, re



def main(argv) :
    directory = argv[0]
    outputFile = open('nboutput.txt','w')

    testFiles = glob.glob(directory + '/**/*.txt', recursive=True)

    modelFile = open('nbmodel.txt','r')
    lines = modelFile.readlines()
    pSpam = float(lines[0].strip('\n'))
    pHam = float(lines[1].strip('\n'))
    spamDict = json.loads(lines[2])
    hamDict = json.loads(lines[3])
    modelFile.close()
    for testFile in testFiles :
        file = open(testFile, 'r', encoding="latin1")
        content = file.read().strip('/n').split()
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in content if len(w.translate(table)) > 0 ]
        pMsgSpam=pMsgHam = 0
        for word in stripped :
            word = word.lower()
            if word not in spamDict or word not in hamDict :
                continue
            pMsgSpam += math.log(spamDict[word])
            pMsgHam += math.log(hamDict[word])
        spamProb = pMsgSpam + math.log(pSpam)
        hamProb = pMsgHam + math.log(pHam)

        if spamProb > hamProb :
            print('spam\t'+testFile,file=outputFile,flush=True)
        else :
            print('ham\t'+testFile,file=outputFile,flush=True)
        file.close()

    outputFile.close()










if __name__== "__main__" :
    main(sys.argv[1:])
