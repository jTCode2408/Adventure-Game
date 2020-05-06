# Write a class to hold player information, e.g. what room they are in
# currently.
#need name, current room, movement method?
##method needs to: check input, move player based on inpuit, print room moved to
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        
    def player_move(self, direction): #method for movement
        if direction == 'n':
            self.cuurent_room = self.current_room.n_to
            print('curent room move', current_room)
        elif direction == 's':
            self.current_room = self.current_room.s_to
            print('curent room move', current_room)
        elif direction == 'e':
            self.current_room = self.current_room.e_to
        elif direction == 'w':
            self.current_room = self.current_room.w_to
            print('curent room move', current_room)   
   
    def __str__(self):
        return f'name: {self.name}, location: {self.current_room}'

    

#player = Player('JT', ['current_room'])
#print(player)