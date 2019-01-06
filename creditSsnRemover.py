'agdsgasgdjgsaif4444-4444-4444-4444hfshg'
import re,pyperclip
def NumRemover():
    text=pyperclip.paste()
    regex_n=re.compile(r'''(
            (\d{3}-\d{2}-\d{4})|
            ((\d{4}|-|)*4)
            )''',re.VERBOSE)
    match=[]
    for dates in regex_n.findall(text):
        match.append(dates[0])
    v=text
    for k in range(0,len(match)):
        v=v.replace(match[k],'')
    print(v)
NumRemover()
        

