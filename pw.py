#insecured password locker program
password={}
import time
import sys
import random
import pyperclip
choose=random.choice('qwertyuiopasdfghjklzxcvbnm][];\',./{}:"<>?1234567890-=!@#$%^&*()_+~')
if len(sys.argv)<2:
    print('how to Use this soft: python pw.py[account name]-copy account password')
    for k  in password.keys():
        password.setdefault(k,choose)
        sys.exit()
account=sys.argv[1]
if account in password:
    pyperclip.copy(password[account])
    input('press v to see the password')
    while 'c':
        pyperclip.paste()
        break
else:
    print('there is no account name such',account)
time.sleep(20)
