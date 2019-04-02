import shelve, pyperclip, sys, re

def checkMadLib(txt):
    RegAdverb = re.compile(r'ADVERB')
    RegVerb = re.complie(r'VERB')
    RegAdjective = re.compile(r'ADJECTIVE')
    RegNoun = re.compile(r'NOUN')

    RegExList = [RegAdverb, RegVerb, RegAdjective, RegNoun]

    for char in RegExList:
        if re.search(txt) == None:
            continue

