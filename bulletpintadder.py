#!python3
#bullet point printer
import time
import pyperclip

text=pyperclip.paste()
lin=text.split('\n')
for i in range(len(lin)):
    lin[i]='*'+lin[i]
text='\n'.join(lin)
pyperclip.copy(text)

