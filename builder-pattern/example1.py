'''
Imagine you are trying to make cars.  Cars have LOTS
of parts.  They have an engine, wheels, doors, brakes, 
seats, etc...  

In order to effectly create a car you have to define
all of those as dependencies in the car constructor
this can be arduous, prone to errors, and easy to lose
track of where in the parameter order you are at

The general rule of thumb, is if the constructor needs 
more than 3 parameters, we want to find a way to abstract
it away.
'''

class Car:
	def __init__(self, brand:str, model:str, engine:str, num_doors:int, fuel_type:str, tires:str):
		self.brand = brand
		self.model = model
		self.engine = engine
		self.num_doors = num_doors
		self.fuel_type = fuel_type
		self.tires = tires

	def __str__(self):
		return "I am a {} {} with a {} motor, {} doors, and {} tires".format(
			self.brand, self.model, self.engine, self.num_doors, self.tires
		)
	

def main():
	f150 = Car("Ford", "F150", "V8", 4, "unleaded", 'all season')
	mustang = Car("Ford", "Mustang", 'V8', 2, None, 'racing')
	challenger = Car("Dodge", "Challenger", "V12", 2, "premium", "all-season")

	print(f150)
	print(mustang)
	print(challenger)

if __name__ == "__main__":
	main()