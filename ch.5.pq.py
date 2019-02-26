#1. What does the code for an empty dictionary look like?
    #{}
#2. What does a dictionary value with a key 'foo' and a value 42 look like?
    #{"foo": 42
#3. What is the main difference between a dictionary and a list?
    #list use indexes to order their data where dictionaries use keys and values
#4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
    #error, invalid key or key not found in spam
#5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
    #'cat' in spam will search for cat in the keys and values where 'cat' in spam.keys() will only look in the keys
#6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
    #'cat' in spam will search for cat in the keys and values where 'cat' in spam.keys() will only look in the values
#7. What is a shortcut for the following code?
    #spam.get('color', 'black')
#if 'color' not in spam:
    #spam['color'] = 'black'

#8. What module and function can be used to “pretty print” dictionary values?
    #module: pprint function: pprint.pprint()