'''

Practice Projects

For practice, write programs to do the following tasks.
Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
Regex Version of strip()

Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
\d+[a-z]+[A-Z]+

'''

import re

def CheckStrength(s):
    #do a for loop that checks capital lower and digit with a regex expreseion for each of the aformentioned criteria
    StrRegexUpperCheck = re.compile(r'([a-z]){1}')
    StrRegexLowerCheck = re.compile(r'([A-Z]){1}')
    StrRegexDigitCheck = re.compile(r'(\d){1}')
    StrRegexLengthCheck = re.compile(r'(\w){8}')

    test = [StrRegexUpperCheck, StrRegexLowerCheck, StrRegexDigitCheck, StrRegexLengthCheck]
    try:
        for i in test:
            print(i.search(s))
    except:
        print('That didnt work')


    #greedyHaRegex = re.compile(r'(Ha){3,5}')
    #mo1 = greedyHaRegex.search(s)
    #print(mo1.group())

CheckStrength('Volcom24')