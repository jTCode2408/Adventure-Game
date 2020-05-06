# Write a class to hold player information, e.g. what room they are in
# currently.
#need name, current room, movement method?
##method needs to: check input, move player based on inpuit, print room moved to
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room=current_room

   
    def __str__(self):
        return f'name: {self.name}, location: {self.current_room}'


player = Player('JT', ['room'])
print(player)