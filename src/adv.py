from room import Room
from player import Player
from items import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['sword']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['lantern']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['rope']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['shovel']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['food']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#ITEMS 
items = {
    'lantern': Item('lantern', 'light source'),
    'rope': Item('rope', 'transportation'),
    'sword': Item('sword', 'weapon'),
    'shovel': Item('shovel', 'for digging'),
    'food': Item('food', 'something to eat'),
  
}

player1 = Player('jt', room['outside']) 
print(player1)

while True:
    nav = input('where would you like to go?: ')  
    if nav == 'q':
        print('thanks for playing!')
        break

    try:
        if nav == 'g' or 'get':
            player1.add_item(room.items)
            
        else:
                print('Keep going then!')
        if nav == 'n': 
            if player1.current_room.n_to != None: 
                player1.current_room = player1.current_room.n_to 
                print(f'MOVED, {player1}')  
            else:
                print('No room north') 
        elif nav == 's':
            if player1.current_room.s_to != None:
                player1.current_room = player1.current_room.s_to
                print(f'MOVED, {player1} ')
            else:
                print('No room south')  
        elif nav == 'e':
            if player1.current_room.e_to != None:
                player1.current_room = player1.current_room.e_to
                print(f'MOVED, {player1} ')
            else:
                print('no room to the east') 
        elif nav == 'w':
            if player1.current_room.w_to != None:
                player1.current_room = player1.current_room.w_to
                print(f'MOVED TO:, {player1} ')
            else:
                print('no room to the west')
        else: #other values enterd
            print('navigation must be [n], [s], [e], or [w]')
          
        
            
    except TypeError:
        print('please enter valid command')
     
