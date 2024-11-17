'''
Now lets put the observer into the store class
and see how it works with the customer form our
first example

The big thing to notice here, is that the store
does NOT know about the customer.  The store could
not care less if the customer exists, or if it is
listening.  It is basically shouting into the void
that it received inventory, and it is not concerned
if anyone is actually listening.
'''
from typing import TypeVar, Callable, Generic
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


T = TypeVar('T')

class EventEnum(Enum):
	INVENTORY = 'INVENTORY'

@dataclass
class Event(Generic[T]):
	event:EventEnum
	data:T

class ObserverInterface(ABC):
	@abstractmethod
	def subscribe(self, subscriber:Callable, event:EventEnum)->None:pass
	@abstractmethod
	def notify(self, event:Event)->None:pass

class Observer(ObserverInterface):
	_subscribers:dict[EventEnum, list[Callable]] = {}

	def subscribe(self, subscriber:Callable, event:EventEnum)->None:
		subs = self._subscribers.get(event)
		if subs is not None:
			subs.append(subscriber)
		else:
			self._subscribers[event] = [subscriber]

	def notify(self, event:Event)->None:
		subscribers = self._subscribers.get(event.event)

		if subscribers is not None:
			for sub in subscribers:
				sub(event.data)

class Item:
	def __init__(self, name:str):
		self.name = name

class Customer:
	def __init__(self, name:str, observer:ObserverInterface):
		self.name = name
		observer.subscribe(self.get_widget, EventEnum.INVENTORY)
		
	def get_widget(self, data:list[Item]):
		for item in data:
			if item.name == "widget":
				print('Hey! my widget Arrived!!!')
	

class Store:
	def __init__(self, observer:ObserverInterface):
		self.observer  = observer

	def receive_inventory(self, inventory:list[Item])->None:
		#do other receiving stuff
		print('receiving inventory')
		[print(item.name) for item in inventory]
		
		self.observer.notify(
			Event[list[Item]](
				EventEnum.INVENTORY, 
				inventory
			)
		)

	

def main():
	observer:Observer = Observer()
	jake:Customer = Customer('Jake', observer)
	store:Store = Store(observer)

	inventory1 = [Item('hammer'), Item('milk'), Item('baseball')]
	inventory2 = [Item('rope'), Item('cheese'), Item('widget')]
	store.receive_inventory(inventory1)
	store.receive_inventory(inventory2)


if __name__ == "__main__":
	main()