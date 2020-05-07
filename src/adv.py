from room import Room
from player import Player
from items import Item

#REPL 
# After each move, the REPL should print the name and description of the player's current room
#Valid commands are n, s, e and w which move the player North, South, East or West
#The parser should print an error if the player tries to move where there is no room.
#REPL. will go somewhere based on user input index in directions list from rooms



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
#
# Main
##ADD ITEMS: attribute = room.items
#hasattr(check if has attribute)
#getattr(if has attribute, get it)

# Make a new player object that is currently in the 'outside' room.
#player object needs: name, location,
player1 = Player('jt', room['outside'],items) 
print(player1)

# Write a loop that:
# * Prints the current description (the textwrap module might be useful here).
while True:
    nav = input('where would you like to go?: ')  # * Waits for user input and decides what to do.
    #bag = input('Add items to inv?: ')
    if nav == 'q': # If the user enters "q", quit the game.
        print('thanks for playing!')
        break

    try:
        if nav == 'g' or 'get':
        #if bag in ['g', 'get', 'take' ]:
            player1.add_item(room.items)
            print(f' NEW INVENTORY: {player1.inventory}')
        else:
                print('Keep going then!')
        if nav == 'n': 
            if player1.current_room.n_to != None: # If the user enters a cardinal direction, attempt to move to the room there.
                player1.current_room = player1.current_room.n_to 
                print(f'MOVED, {player1}')  # * Prints the current room name
            else:
                print('No room north') # Print an error message if the movement isn't allowed.
        elif nav == 's':
            if player1.current_room.s_to != None:
                player1.current_room = player1.current_room.s_to
                print(f'MOVED, {player1} ')
            else:
                print('No room south')    #if no room
        elif nav == 'e':
            if player1.current_room.e_to != None:
                player1.current_room = player1.current_room.e_to
                print(f'MOVED, {player1} ')
            else:
                print('no room to the east') 
        elif nav == 'w':
            if player1.current_room.w_to != None:
                player1.current_room = player1.current_room.w_to
                print(f'MOVED, {player1} ')
            else:
                print('no room to the west')
        else: #other values enterd
            print('naigation must be [n], [s], [e], or [w]')
            #get item
        
            
    except TypeError:
        print('please enter valid  command')
        #if invakid entry,
