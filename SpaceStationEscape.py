from sys import exit

PROMPT = "> "

class Thing:

	def __init__(self, isMoveable, name, description):
		self.isMoveable = isMoveable
		self.name = name
		self.description = description

class Agent:
	possessions = []

	def __init__(self, name, location):
		self.name = name
		self.location = location

	def isLocatedAt(self, location):
		return (self.location == location)

	def possesses(self, object):
		return (object in self.possessions)

	def look(self, thing):
		if self.isLocatedAt(thing) or thing in self.possessions:
			message("A " + thing.name + ". " + thing.description)
		else:
			message("From this distance, it just looks like a " + thing.name)
	
	def move(self, thing):
		message("You float over to the " + thing.name)
		self.location = thing

	def take(self, thing):
		if not self.location == thing:
			message("You can't reach a " + thing.name + " from here.")
		elif not thing.isMoveable:
			message("You can't move the " + thing.name)
		else:
			message("You have picked up the " + thing.name)
			self.possessions.append(thing)

	def use(self, thing):
		if self.location != thing and not thing in self.possessions:
			message("You can't seem to reach that.")

		elif not thing.isMoveable:
			message("You try, but it won't budge.")

		elif thing == spacesuit:
			self.possessions.append(thing)
			message("You have put on the " + thing.name + ". The display on your arm shows all green.")

		elif thing == wrench:
			self.possessions.append(thing)
			if self.location == window:
				message("""You smash the window.
	There is a roaring rush of air.
	You are pulled outside into open space.""")
				for possesion in self.possessions:
					if possesion.name == "spacesuit":
						survivalEnding()
				spacedEnding()
			elif self.location == door:
				message("""There are no visible bolts.
	You try jamming the wrench in the cracks.
	It doesn't work.""")
			else:
				message("There's nothing here a wrench could be used on.")
		else:
			message("You don't know how to use a " + thing.name + " here.")


def message(string):
	print("\n\t" + string + "\n")

def survivalEnding():
	message("""You catch your breath as as shattered glass floats by.
	The space suit continues to show all green on the display.
	You activate the jets to move towards your shuttle.
	
		You live to breathe another day.""")
	end()

def spacedEnding():
	message("""Your unprotected body flops in the emptiness.
	Your lungs implode as as your eyes bulge.
	Your death isn't pretty.""")

	message("""That's okay.

		No one is there to see it.""")
	end()

def game():
	while(True):
		inputString = input(PROMPT).split(" ")
		if len(inputString) == 1:
			if inputString[0] == "exit":
				end()
		elif len(inputString) == 2:
			action = actionMap.get(inputString[0])
			thing = thingMap.get(inputString[1])
			if action:
				if thing:
					action(thing)
				else:
					message(inputString[0] + " what?")
			else:
				message("I don't know how to " + inputString[0])
		else:
			continue


def end():
	exit(0)


# setup
wrench = Thing(True, "wrench", "A substantial thing.")
room = Thing(False, "room", "It's surpisingly large for what you assume is a space station.")
window = Thing(False, "window", "About the width of your shoulders. Looks dangerously thin.")
spacesuit = Thing(True, "spacesuit", "Looks designed to be used for EVAs.")
wall = Thing(False, "wall", "White, with alternating padding and rails for zero-g maneuvering.")
door = Thing(False, "door", "There is no visible way to open it. Must be locked from the other side.")
mickey = Agent("Mickey", room)

thingMap = {"wrench":wrench, "room":room, "window":window, "spacesuit":spacesuit, "suit":spacesuit, "door":door, "wall":wall, "walls":wall}
actionMap = {"look":mickey.look, "take":mickey.take, "move":mickey.move, "use":mickey.use}
againMap = {"y":game, "n":end}

message("""You awake to find yourself floating, weightless.
	Starlight spills through a small window,
	scattering across the padded white walls.
	A bulky monkru wrench slowly drifts by
	the shimmery faceplate of a spacesuit.
	The door across from you has no features save
	a flashing red light by a small label that reads
	
		--- Low Pressure Warning ---""")

print("You can look, take, move, and use.")
print(" [verb] [noun]")
game()