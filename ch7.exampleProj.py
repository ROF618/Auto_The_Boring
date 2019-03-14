#Regex can not count do not try and count with regex
#if you preface regex expression with r, python knows the / will mean what is usually means in regex aka it will be double /
#? means optional in regex unless its after {}
#^ means not the range specified but if it used at the beginning of the range it specifies that the information that is being looked for needs to be at the beginning
#when | key is used in the second part of the regex expression e.g (re.compile('foo', re.IGNORECASE | re.DOTALL) to specify that you want both of the directives to execute on the expression
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)group())

emailRegex = re.compile(r'''(
      [a-zA-Z0-9._%+-]+      # username
      @                      # @ symbol
      [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
        )''', re.VERBOSE)


# Find matches in clipboard text.
   text = str(pyperclip.paste())
 matches = []
 for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
 for groups in emailRegex.findall(text):
       matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')