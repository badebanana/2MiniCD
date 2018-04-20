class Room:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def createNewRoom(self, name):
        newRoom = Room(name)

    def addUser(self,client):
        if client.lower() not in self.clients:
            self.clients.append(client)


    def __str__(self):
        print('#',self.name)
        print(self.clients)