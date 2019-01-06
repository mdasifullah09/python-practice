import time
inventory={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
item_number=0
print('Inventory:')
for i,v in inventory.items():
    print(str(v), i)
    item_number=item_number+inventory.get(i,0)
print('Total number of item:',item_number)
stuff={'rope':1,'rope':4,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
def PrintInventory(stuffy):
    item_number=0
    print('Inventory:')
    for k,v in inventory.items():
        print(str(v),k)
        item_number=item_number+v
    print('Total number of Inventory:',item_number)
PrintInventory(stuff)
time.sleep(20)
