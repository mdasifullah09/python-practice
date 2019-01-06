import re,pyperclip
def dateremover():
    text=pyperclip.paste()
    regex_d=re.compile(r'''(
            (\d/\d{2}/\d{4})|
            (\d{2}-\d{2}-\d{4})|
            (\d{4}/\d{2}/\d{2})
            )''',re.VERBOSE)
    match=[]
    for dates in regex_d.findall(text):
        match.append(dates[0])
    v=text
    for k in range(0,len(match)):
        v=v.replace(match[k],'')
    print(v)
        
dateremover()
'asajg3/03/2015hdakxz02-02-2016dshk2015/02/15'

