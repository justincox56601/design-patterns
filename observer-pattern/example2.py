'''
We can quickly see several problems here.

1) this is not maintainable.  Everytime we want to
add a new customer we will need to create a new
class property to hold the reference, AND we will
have to add a new if statement in the get_inventory
method to check for it.  

2) the store class is now tightly coupled with the 
concept of the customer.  It has to know of the 
customer(s) and carry a reference to it.  event though
it is only needed rarely.

3) the number of customers is completely open ended.
At any time, there could be 0 or a bajillion customers
and our current system has no way to handle that.

This is where the observer pattern shines.  We will
create an observer whose job is to store a list of
of subscribers and the events they are subsribed to.
Then when an event happens, the obersever will notify 
the correct subscribers and only the correct subscribers.

To simplify things, this example will ONLY look at the 
Observer class and it's usage

The Observer() class stores a dictionary that uses 
EventEnum as the keys, and the values are a list of
subscribers.  The subscribers are callable functions.

The subscribe() method is responsible for storing the 
subscriber under the appropriate dictionary key.

The notify method receives an Event.  The then grabs
all of the subscribers to that event, and calls the 
subscriber functions passing in the data parameter.

This way, no mater which event happens, only the subscribers
subscribed to that specific event are notified.  More
importantly, these notifications happen ONLY when an 
event happens.  There is no continual loop or checking
if a specific event happened.
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

def print_inventory(items:list[Item]):
	for item in items:
		print(item.name)

def main():
	observer:Observer = Observer()
	inventory1:list[Item] = [Item('widget'), Item('Hammer'), Item('toothpaste')]

	observer.subscribe(print_inventory, EventEnum.INVENTORY)
	observer.notify(Event[list[Item]](EventEnum.INVENTORY, inventory1))

if __name__ == "__main__":
	main()