import tuple    
def printPicnic(itemsDict,leftWidth,rightWidth):
    print('picnic item:'.center(leftWidth+rightWidth))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'-'),v.rjust(rightWidth,'-'))
itemsDict={'sandwich':'4','club-sandwhich':'5','hotDog':'2'} 
printPicnic(itemsDict,10,0)
itemsDict={'sandwich':'7','club-sandwhich':'9','hotDog':'3'} 
printPicnic(itemsDict,10,0)
    
d='hello world'
print(d.strip())
time.sleep(20)
