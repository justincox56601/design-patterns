'''
The observer pattern is a behavoiral pattern 
used to handle one-to-many relatinships without
making the objects tightly coupled

Imagine a scenario where you own a physical store.
One day a customer comes in wants a widget.  You 
are currenlty out of that widget.  You have two options
you can hvae your customer come back every single day
until you get that widget.  meaning they will put in 
a lot of work for nothing until the one time the widget does 
arrive.  Or you can, in addition to everything else you 
do in your store, keep track of that customer and notify them
when the item arrives.

Obviously being the great store owner you are, you opt for
the second option.  it is easy enough at first.  you simply
add a little check everytime you receive inventory.  If your 
inventory includes the widget, you will notify your customer.
'''

class Customer:
	def __init__(self, name:str):
		self.name = name

class Item:
	def __init__(self, name:str):
		self.name = name

class Store:
	_customer = None

	def track_customer(self, customer:Customer)->None:
		self._customer = customer

	def get_inventory(self, inventory:list[Item])->None:
		for item in inventory:
			print('receiving {}'.format(item.name))
			#receive inventory stuff
			if item.name == 'widget':
				self.notify(self._customer, 'widget')

	def notify(self, customer:Customer, item:str)->None:
		print('{}, your {} has arrived.'.format(customer.name, item))

def main():
	customer = Customer("Jack")
	store = Store()
	inventory1 = [Item('hammer'), Item('milk'), Item('baseball')]
	inventory2 = [Item('rope'), Item('cheese'), Item('widget')]

	store.track_customer(customer)
	store.get_inventory(inventory1)
	store.get_inventory(inventory2)

if __name__ == "__main__":
	main()