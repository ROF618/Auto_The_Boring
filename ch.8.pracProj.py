import re

openTXTFile = open('./hello.txt')

def MadLibMaker(IncomingText):
    ADJectiveCheck = re.compile(r'adjective', re.IGNORECASE)
    NounCheck = re.compile(r'noun', re.IGNORECASE)
    ADVCheck = re.compile(r'adverb', re.IGNORECASE)
    VerbCheck = re.compile(r'verb', re.IGNORECASE)
    splitIncomingText = IncomingText.read().split(' ')
    for char in splitIncomingText:
        if NounCheck.search(char) == None:
            print("the if evaluates to true")

        else:
            print(char)



MadLibMaker(openTXTFile)