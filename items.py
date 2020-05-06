#name and desc attributes
#base class where speciealized items will be added
'''Add an on_take method to Item.
#def ontake
Call this method when the Item is picked up by the player.
if player picks up item.name:(using get)
on_take should print out "You have picked up [NAME]" when you pick up an item.
#print you have item.name when picked up
The Item can use this to run additional code when it is picked up.

Add an on_drop method to Item. Implement it similar to on_take.

Implement support for the verb drop followed by an Item name. This is the opposite of get/take.
'''
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'ITEM, {self.name} {self.description}'

    def on_take():


myItem = Item('laptop', 'vivobook')
print(myItem)