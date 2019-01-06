inv={'rope':1,'gold coin':32}
dragonLoot=['gold coin','dagger','gold coin','ruby']
def AddtoInventory(inventory,addItems):
    item_number=0
    count={}
    for i in  dragonLoot:
        count.setdefault(i,0)
        count[i]+count[i]+1
    added={**count,**inv}
    print('Inventory:')
    for k,v in added.items():
        print(str(v),k)
        item_number=item_number+v
    print('Total number of Inventory:',item_number)
AddtoInventory(inv,dragonLoot)

