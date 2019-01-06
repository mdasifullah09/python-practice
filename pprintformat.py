import pprint
msg='i need money and peace'
count={}
for char in msg:
    count.setdefault(char,0)
    count[char]=count[char]+1
pprint.pprint(count)

