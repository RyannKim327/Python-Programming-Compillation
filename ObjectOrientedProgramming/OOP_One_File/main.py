class room:
	def __init__(self, roomname="Computer Laboratory"):
		self.currentRoom = roomname
	def getRoom(self):
		return self.currentRoom
	def setRoom(self, roomname="Computer Laboratory"):
		self.currentRoom = roomname

room1 = room()
room2 = room("Computer Laboratory 2")
print(room1.getRoom())
print(room2.getRoom())

room1.setRoom("Audio Visual Room")
room2.setRoom("Administrator")

print(room1.getRoom())
print(room2.getRoom())
