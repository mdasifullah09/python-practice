import re
string=re.compile(r'^\d[x]$')
match=string.search('1x')
print(match.group())
dotstar=re.compile(r'(<.*?>)')
prnt=dotstar.search("<dhk>ashd>shdk>")
print(prnt.group())
escap=re.compile(r'love 1:(.*) love 2:(.*) love 3:(.*)  love 4:(.*)')
fnd=escap.search('love 1: slowfuck love 2: deepfuck love 3: blowfuck  love 4: most importantly chichingfuck')
print(fnd.group(4))
"""string='i love milk but my milk is sucking by other the mil i am drinking is not the one that i want i want my milk [naz]'
count={}
for char in string:
    count.setdefault(char,0)
    print(count)
    count[char]=count[char]+1
print(count)
print('back to the study')"""
string='i love milk but my milk is sucking by other the milk

i am drinking is not the one that i want i want my milk [naz]'
love=re.compile(r'NAZ',re.I)
print(love.search(string).group())
