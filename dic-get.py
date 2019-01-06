import time
book={'algo':'deitel','data-mining':'chapel','ooad':'scrudinger'}
print('i want the book of ',book.get('algorith',0))
name=input('enter book name')
if name not in book:
    book.setdefault(name,'jack')
    print(book)
message='I want peace and money for the lifetime.'
count={}
for character in message:
    print(character)
time.sleep(10)
