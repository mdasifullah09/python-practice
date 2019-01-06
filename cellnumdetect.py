#!python 3
#phone number detector
import time
import re
def definecellnum(msg):
    phonenum=re.compile(r'((\d{3}\))-(\d{3}-\d{4})')
    cell= phonenum.search(msg)
    print('you gotta cell match',cell.group(1))
message=input('leave your massage you may provoide your cell number\n')
definecellnum(message)

