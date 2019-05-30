import re

openTXTFile = open('./hello.txt')

def MadLibMaker(IncomingText):
    ADJectiveCheck = re.compile(r'adjective', re.IGNORECASE)
    NounCheck = re.compile(r'noun', re.IGNORECASE)
    ADVCheck = re.compile(r'adverb', re.IGNORECASE)
    VerbCheck = re.compile(r'verb', re.IGNORECASE)
    splitIncomingText = IncomingText.read().split(' ')
    userInput = []

    for char in splitIncomingText:
        if NounCheck.search(char) is not None:
            print("Please input a Noun")
            userNoun = input()
            userInput.append(userNoun)
        elif ADJectiveCheck.search(char) is not None:
            print("Please input a adjective")
            userAdjective = input()
            userInput.append(userAdjective)
        elif ADVCheck.search(char) is not None:
            print("Please input a Adverb")
            userADV = input()
            userInput.append(userADV)
        elif VerbCheck.search(char) is not None:
            print("Please input a Verb")
            userVerb = input()
            userInput.append(userVerb)
        else:
            userInput.append(char)

    print(' '.join(userInput))



MadLibMaker(openTXTFile)