class CoffeeMachine:

	WATER_LEVEL = 100

	def _start_machine(self):
		# starts the mathine
		if self.WATER_LEVEL > 20:
			return True
		else:
			print("Please add water")
			return False

	def __boil_water(self):
		# boils the water!
		return "boiling..."

	def make_coffee(self):
		# yum, a goog coffee!
		if self._start_machine():
			self.WATER_LEVEL -= 20
			print(self.__boil_water())
			print("Coffee is ready my dear!")

machine = CoffeeMachine()

#for i in range(0, 5):
#	machine.make_coffee()

print("Make coffee: Public", machine.make_coffee())
print("Start machine: Protected", machine._start_machine())
print("Boil water: Private", machine._CoffeeMachine__boil_water())