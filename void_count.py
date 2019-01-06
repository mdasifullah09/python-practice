'''
XXXX                XXXXX 
XXX               XXXXXXX
XXXXX                XXXX
XX                 XXXXXX
.                       .
.                       .
.                       .
XXXX                 XXXX
XXX                XXXXXX
'''
def void_count():
    r=int(input('Enter the number of row as your wish>0 :\n'))
    for k in range(1,r+1):
        print('\n',end='')
        for i in range(1,25):
            x=input()
            print(x.count(' '))
            print(x.strip('\n'))
            
void_count()
