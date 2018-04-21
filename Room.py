class Room:
    def __init__(self, name, moderador):
        self.name = name
        self.clients = []
        if moderador == "":
            self.moderador = ""
        else:
            self.moderador = moderador
        self.addUser(moderador)

    def addUser(self,client):
        if client.lower() not in self.clients:
            self.clients.append(client)

    def __str__(self):
        print('---------------------------------------------')
        print('#',self.name)
        print(self.clients)
        print('Moderador:',self.moderador)

    def roomName(self):
        return self.name

    def removeClient(self, name):
        self.clients.remove(name)
