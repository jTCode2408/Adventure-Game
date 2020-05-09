# Write a class to hold player information, e.g. what room they are in
# currently.
#need name, current room, movement method?
##method needs to: check input, move player based on inpuit, print room moved to
class Player():
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        return f'NEW INVB: {self.inventory}'
     

    
        
   

    def __str__(self):
        return f'Playername: {self.name}, location: {self.current_room} Inv: {self.inventory}'


#player = Player('JT', ['current_room'])
#print(player)