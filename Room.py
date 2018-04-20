class Room:
    def __init__(self, name):
        self.name = name

    def createNewRoom(self, name):
        newRoom = Room(name)

    def __str__(self):
        print('#',self.name)