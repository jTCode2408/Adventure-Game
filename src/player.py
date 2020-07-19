
class Player():
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        return f'NEW INV: {self.inventory}'
     
    def __str__(self):
        return f'Playername: {self.name}, location: {self.current_room} '

