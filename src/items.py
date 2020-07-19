
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
