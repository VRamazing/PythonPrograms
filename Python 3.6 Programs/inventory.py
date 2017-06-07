stuff = {'rope' : 1 , 'torch' : 6 , 'gold coin' : 42 , 'dagger' : 1 , 'arrow':12}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
def displayInventory(inventory):
	print('Inventory :')
	item_total = 0
	for k,v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("TOtal number of items : " + str(item_total))
	
displayInventory(stuff)

def addToInventory(inventory,addedItems):
	for i in dragonLoot:
		if i in inventory.keys():
			inventory[i]+=1
		else:
			inventory[i]=1


addToInventory(stuff,dragonLoot)
displayInventory(stuff)