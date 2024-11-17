from abc import ABC, abstractmethod
from typing import Self
'''
lets take this one step further and say we have a car
manuafacturing facility. I know this is contrived but 
stick with me.

Say we have a ford facility, and this particular facility
makes Ford F150s and mustangs.  Not just one F150 or mustang, but all sorts of them.
In this case, we can extend our CarBuilder and create a 
F150Builder().  This builder will make specifially F150s
but since many of the things about them will be the same, 
we can put the defaults into the F150Builder()
'''


class Car:
	def __init__(self, brand:str, model:str, trim:str, engine:str, num_doors:int, fuel_type:str, tires:str):
		self.brand = brand
		self.model = model
		self.trim = trim
		self.engine = engine
		self.num_doors = num_doors
		self.fuel_type = fuel_type
		self.tires = tires

	def __str__(self):
		return "I am a {} {} {} with a {} motor, {} doors, and {} tires".format(
			self.brand, self.model, self.trim, self.engine, self.num_doors, self.tires
		)

class CarBuilderInterace(ABC):
	@abstractmethod
	def brand(self, brand:str)->Self:pass
	@abstractmethod
	def model(self, model:str)->Self:pass
	@abstractmethod
	def trim(self, trim:str)->Self:pass
	@abstractmethod
	def engine(self, engine:str)->Self:pass
	@abstractmethod
	def doors(self, num_doors:int)->Self:pass
	@abstractmethod
	def fuel(self, fuel_type:str)->Self:pass
	@abstractmethod
	def tires(self, tires:str)->Self:pass
	@abstractmethod
	def build(self)->Car:pass

class CarBuilder(CarBuilderInterace):
	_brand = None
	_model = None
	_trim = None
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
	
	def trim(self, trim:str)->Self:
		self._trim = trim
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
			self._brand, self._model, self._trim, self._engine, self._num_doors, self._fuel_type, self._tires
		)

class FordFacilty:
	def build_f150(self)->None:
		base = self.F150Builder().trim("SE").build()
		extCab = self.F150Builder().trim('Extended Cab').doors(4).build()
		sport = self.F150Builder().trim("Sport").engine("V12").build()

		print(base)
		print(extCab)
		print(sport)

	def build_Mustang(self)->None:
		se = self.MustangBuilder().trim("SE").build()
		lx = self.MustangBuilder().trim("LX").build()
		sport = self.MustangBuilder().trim('Sport').tires("racing").engine('V12').build()

		print(se)
		print(lx)
		print(sport)

	#these could have been thier own classes
	#but since they are specific to the FordFacilty
	#class, I feel making them sub classes better
	#highlights the organizational structure
	class F150Builder(CarBuilder):
		_brand = 'Ford'
		_model = 'F150'
		_engine = 'V8'
		_num_doors = 2
		_fuel_type = 'unleaded'
		_tires = 'all season'

	class MustangBuilder(CarBuilder):
		_brand = 'Ford'
		_model = 'Mustang'
		_engine = 'V8'
		_num_doors = 2
		_fuel_type = 'premium'
		_tires = 'all season'
	

def main():
	facility = FordFacilty()
	facility.build_f150()
	facility.build_Mustang()

if __name__ == "__main__":
	main()