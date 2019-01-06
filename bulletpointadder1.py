import pyperclip
txt='My name is asif\
skndksafi sdkkjfhbs\
eshiwjidegfwdwiuhf'
pyperclip.copy(txt)
for i in range(len(txt)):
    txt[i]='*'+txt[i]
    print(txt[i])

