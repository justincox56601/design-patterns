'''
I am aware that in Python and a few other languages
named parameters are a thing, and this aleviates 
most of this problem. But that is not the case with
all languages so we are going to look at a different
solution to this problem.

The main problem we are trying to solve is how to 
abstract away this construction process so we don't
have to do it every time, and make it less prone to
human error?

One viable solution is to hide all of the properties in 
a props paramter like a dictionary. But now, we still have
a large constructor, and we do need to do null checking 
because we can't guarantee that every property that is needed
is present.

We could create an interface to make each parameter required, 
and that is the case in languages that use traditional
interfaces.  I could have implemented it here, but it wouldn't
have helped our situation much

However, now our Car() construction is cleaner, and easier to read.
'''


class Car:
	def __init__(self, props:dict):
		
		self.brand = props['brand'] or None
		self.model = props['model'] or None
		self.engine = props['engine'] or None
		self.num_doors = props['num_doors'] or None
		self.fuel_type = props['fuel_type'] or None
		self.tires = props['tires'] or None

	def __str__(self):
		return "I am a {} {} with a {} motor, {} doors, and {} tires".format(
			self.brand, self.model, self.engine, self.num_doors, self.tires
		)
	

def main():
	f150 = Car({
		"brand":"Ford",
		"model":"F150",
		"engine":"v8",
		"num_doors": 4,
		"fuel_type": 'unleaded',
		"tires":"all season"
	})
	

	print(f150)

if __name__ == "__main__":
	main()