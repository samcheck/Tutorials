
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	totalItems = 0
	print('-----------------------------')
	print('Inventory:')
	for k, v in inventory.items():
		print(str(v), k)
		totalItems += v
	
	print('Total number of items: ' + str(totalItems))
	print('-----------------------------')

displayInventory(stuff)

def addToInventory(inventory, addedItems):
	for item in addedItems:
		if item in inventory.keys():
			inventory[item] += 1
		else:
			inventory.setdefault(item, 1)
	return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['rope', 'dagger', 'gold coin', 'gold coin', 'ruby']
invNew = addToInventory(inv, dragonLoot)

displayInventory(invNew)
