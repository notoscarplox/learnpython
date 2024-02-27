inventoryItems = {'rope': 1,
                  'torch': 6,
                  'gold coin': 42,
                  'dagger': 1,
                  'arrow': 12}

dragonLoot = ['gold coin',
              'dagger',
              'gold coin',
              'gold coin',
              'ruby']


# Display the Inventory
def displayInventory(inventory):
    totalitems = 0
    for k, v in inventory.items():
        print(F"{k}: {v}")
        totalitems = totalitems + v

    print(f"Total: {totalitems}")


# Add new items to the Inventory
def addToInventory(loot, inventory):
    for stuff in loot:
        if stuff in inventory:
            inventory[stuff] = inventory[stuff] + 1
        else:
            inventory[stuff] = 1


addToInventory(dragonLoot, inventoryItems)
displayInventory(inventoryItems)
