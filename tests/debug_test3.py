# to test pdb on
from remote_pdb import RemotePdb
RemotePdb("localhost", 4444).set_trace()

# testing pdb with objects
class Lunchbox:
	def __init__(self, owner="No name", drink="No drink", sandwich="No sandwich", snack="No snack"):
		self.owner = owner
		self.drink = drink
		self.sandwich = sandwich
		self.snack = snack

	def printLunch(self):
		print("Hello " + self.owner +". Your lunch for today will be a " +
				self.sandwich + " sandwich, some " + self.drink + ", and " +
				self.snack + " for a snack.\n")

	def swapLunchContents(self, boxToSwap, printAboutSwap):
		tempDrink = boxToSwap.drink
		tempSandwich = boxToSwap.sandwich
		tempSnack = boxToSwap.snack
		boxToSwap.drink = self.drink
		boxToSwap.sandwich = self.sandwich
		boxToSwap.snack = self.snack
		self.drink = tempDrink
		self.sandwich = tempSandwich
		self.snack = tempSnack
		if (printAboutSwap):
			print self.owner + " is swapping their lunch with " + boxToSwap.owner + "'s!\n"

lb1 = Lunchbox("Jasons", "milk", "lettuce & seeds", "cheese cubes")
lb2 = Lunchbox("Randles", "coca cola", "cheese puffs", "three big donuts")
lb1.printLunch()
lb2.printLunch()
lb1.swapLunchContents(lb2, True)
lb1.printLunch()
lb2.printLunch()
