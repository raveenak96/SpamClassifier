import sys,os,glob,json

def main(argv) :
    directory = argv[0]
    inputFile = open(directory, 'r')

    lines = inputFile.readlines()
    if len(lines) ==0 :
        sys.exit(0)

    #true label:0, predicted label:1
    results = []
    trueSpam=trueHamPredSpam=trueHam=trueSpamPredHam=0
    for line in lines :
        lineVals = line.strip('\n').split()
        if 'spam' in lineVals[1] :
            if lineVals[0]=='spam' :
                trueSpam += 1
            else :
                trueSpamPredHam += 1
        elif 'ham' in lineVals[1] :
            if lineVals[0]=='ham' :
                trueHam += 1
            else :
                trueHamPredSpam += 1

    spamPrec = trueSpam / (trueSpam + trueHamPredSpam)
    spamRec = trueSpam / (trueSpam + trueSpamPredHam)
    spamF1 = 2 * ( (spamPrec * spamRec) / (spamPrec + spamRec))

    hamPrec = trueHam / (trueHam + trueSpamPredHam)
    hamRec = trueHam / (trueHam + trueHamPredSpam)
    hamF1 = 2 * ( (hamPrec * hamRec) / (hamPrec + hamRec))

    print('Spam Precision: '+str(spamPrec))
    print('Spam Recall: '+str(spamRec))
    print('Spam F1-score: '+str(spamF1))
    print('Ham Precision: ' + str(hamPrec))
    print('Ham Recall: ' + str(hamRec))
    print('Ham F1-score: ' + str(hamF1))

if __name__== "__main__" :
    main(sys.argv[1:])