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
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.description = item_description

    def __str__(self):
        return f'ItemName{self.item_name} ItemDescipt{self.item_description}'

    def on_take(self):
        print(f'You have picked up {self.item_name}')

    def on_drop(self):
        print(f'You have picked up {self.item_name}')


#myItem = Item(['laptop', 'vivobook' 'tv', 'sony', 'ipod', 'apple'])
#print(myItem)