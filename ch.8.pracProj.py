import re

openTXTFile = open('./hello.txt')

def MadLibMaker(IncomingText):
    ADJectiveCheck = re.compile(r'adjective', re.IGNORECASE)
    NounCheck = re.compile(r'noun', re.IGNORECASE)
    ADVCheck = re.compile(r'adverb', re.IGNORECASE)
    VerbCheck = re.compile(r'verb', re.IGNORECASE)
    splitIncomingText = IncomingText.read().split(' ')

    for char in splitIncomingText:
        if NounCheck.search(char) is not None:
            print("Please input a Noun")
            userNoun = input()
            print(userNoun)
        elif ADJectiveCheck.search(char) is not None:
            print("Please input a adjective")
            userAdjective = input()
            print(userAdjective)
        elif ADVCheck.search(char) is not None:
            print("Please input a Adverb")
            userADV = input()
            print(userADV)
        elif VerbCheck.search(char) is not None:
            print("Please input a Verb")
            userVerb = input()
            print(userVerb)
        else:
            print(char)



MadLibMaker(openTXTFile)