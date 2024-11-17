from abc import ABC, abstractmethod
from typing import Self
'''
In other languages we could use overloaded constructors
so that it can take any number of parameters we send.
Python doesn't have that ability so I wont be showing it.

But more over, we still have the problem of having too
many properties to deal with every time we create a Car()

This is where the builder pattern comes in.  We can create
a builder object that will allow us to build a car with only
the pieces we want and in any order.

Now the actual creation of the Car() object is abstracted away
and we only need to focus on the parts of Car() object that 
matter at the time we are creating it.
'''

class BuilderInterface(ABC):
	@abstractmethod
	def build(self):pass

class CarBuilderInterace(BuilderInterface):
	@abstractmethod
	def brand(self, brand:str)->Self:pass
	@abstractmethod
	def model(self, model:str)->Self:pass
	@abstractmethod
	def engine(self, engine:str)->Self:pass
	@abstractmethod
	def doors(self, num_doors:int)->Self:pass
	@abstractmethod
	def fuel(self, fuel_type:str)->Self:pass
	@abstractmethod
	def tires(self, tires:str)->Self:pass
	@abstractmethod
	def build(self):pass


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
	
class CarBuilder(CarBuilderInterace):
	_brand = None
	_model = None
	_engine = None
	_num_doors = None
	_fuel_type = None
	_tires = None
	
	def brand(self, brand:str)->Self:
		self._brand = brand
		return self
	
	def model(self, model:str)->Self:
		self._model = model
		return self
	
	def engine(self, engine:str)->Self:
		self._engine = engine
		return self
	
	def doors(self, doors:int)->Self:
		self._num_doors = doors
		return self
	
	def fuel(self, fuel_type:str)->Self:
		self._fuel_type = fuel_type
		return self
	
	def tires(self, tires:str)->Self:
		self._tires = tires
		return self
	
	def build(self)->Car:
		return Car(
			self._brand, self._model, self._engine, self._num_doors, self._fuel_type, self._tires
		)


	

def main():
	f150 = CarBuilder().brand("Ford").model("F150").engine("V8").doors(2).build()
	mustang = CarBuilder().brand('Ford').doors(2).fuel('premium').model("Mustang").build()
	
	print(f150)
	print(mustang)

if __name__ == "__main__":
	main()