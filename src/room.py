class Room():
    def __init__(self, name,description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    
    def __str__(self):
        return f'RoomName: {self.name}, RoomDescript: {self.description} ItemsInRoom: {self.items}'

