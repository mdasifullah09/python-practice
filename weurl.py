#!python3
#regex pattern matching
import re
import pyperclip
def weburl():
    text=pyperclip.paste()
    match=[]
    url_regex=re.compile(r'''(
        [http://]+
        [https://]+
        [www\.]+
        [\w+\.]+
        (\.[a-zA-Z]{2,3})
        )''',re.VERBOSE)
    for groups in url_regex.findall(text):
        match.append(groups[0])
    if len(match) > 0:
        print('\n'.join(match))
    else:
        print('found no match')
weburl()

