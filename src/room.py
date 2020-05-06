# Implement a class to hold room information. This should have name and
# description attributes.
#The room should have name and description attributes.
#The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.
#s_to = room[name]
'''
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
'''

class Room():
    def __init__(self, room,description, n_to, s_to, w_to, e_to):
        self.room = room
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = [room].e_to
        self.w_to = w_to

    def __str__(self):
        return f'rooms: {self.room}, descript: {self.description}, moves: {self.n_to} {self.s_to}, {self.e_to} {self.w_to}'
