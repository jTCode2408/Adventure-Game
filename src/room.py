# Implement a class to hold room information. This should have name and
# description attributes.
#The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

#ability to add items to rooms
##list that holds items in room
##add functionality to main loop to print items in room when player enter


class Room():
    def __init__(self, name,description, items):
        self.name = name
        self.description = description
        self.items = items

        self.n_to = None #will be dif rooms dep on user location. none for now
        self.e_to = None
        self.s_to = None
        self.w_to = None

    
    def __str__(self):
        return f'room: {self.name}, descript: {self.description} items: {self.items}'

