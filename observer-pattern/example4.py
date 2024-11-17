'''
There are a couple problems right now. The
first glaring one, is that as it stands, the
customer is being notified every single time
inventory is received. regardless of whether 
the widget is in there or not.

The second problem is the user is now going
to get notified every time a widget comes in.
They only care about the one widget, and don't
want to be notified after they get their first
one.

To solve these problems we are going to add in 
an unsubscribe method, and add in a new handler 
that will listen for inventory, and then re-notify
the observer with the specific item we are looking 
for.

In this example we added an InventoryManager (and
interface) an and ItemEnum.  This allows the inventory
to have a dedicated handler and decouple that from the 
store.  The Inventory manager will receive inventory, 
do the otehr stuff it needs to, and then notify the 
observer of each item it received.

We also updated the store to have a subscribe_to_item
method.  this takes the observer away from the customer
and puts the responsibility of subscribing to the item
back on the store.  Notice, the store still does not
need to keep track of the customer.  The function receives
a subscriber, wraps it in a lamda function so it can
unsubscribe after the item notification happens, and then
subscribes to the specific item the customer wants.

Now the customer ONLY gets notified when the specific
item they want arrives, AND they only get notified once.
'''
from typing import TypeVar, Callable, Generic
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


T = TypeVar('T')

class EventEnum(Enum):
	INVENTORY = 'INVENTORY'

class ItemEnum(Enum):
	HAMMER ='HAMMER'
	ROPE = 'ROPE'
	WIDGET = 'WIDGET'
	BASEBALL = 'BASEBALL'
	CHEESE = 'CHEESE'	


@dataclass
class Event(Generic[T]):
	event:Enum
	data:T

class ObserverInterface(ABC):
	@abstractmethod
	def subscribe(self, subscriber:Callable, event:Enum)->None:pass
	@abstractmethod
	def unsubscribe(self, subscriber:Callable, event:Enum)->None:pass
	@abstractmethod
	def notify(self, event:Event)->None:pass

class Observer(ObserverInterface):
	_subscribers:dict[Enum, list[Callable]] = {}

	def subscribe(self, subscriber:Callable, event:Enum)->None:
		subs = self._subscribers.get(event)
		if subs is not None:
			subs.append(subscriber)
		else:
			self._subscribers[event] = [subscriber]
		
	
	def unsubscribe(self, subscriber:Callable, event:EventEnum)->None:
		subs = self._subscribers.get(event)
		if subs is not None:
			subs.remove(subscriber)
			if len(subs)==0:
				del self._subscribers[event]

	def notify(self, event:Event)->None:
		subscribers = self._subscribers.get(event.event)

		if subscribers is not None:
			for sub in subscribers:
				sub(event.data)

class Item:
	def __init__(self, name:ItemEnum):
		self.name = name

class InventoryManagerInterface(ABC):
	@abstractmethod
	def receive(self, inventory:list[Item])->None:pass
	@abstractmethod
	def notify_item_received(self, item:Item)->None:pass

class InventoryManager(InventoryManagerInterface):
	def __init__(self, observer:Observer):
		self.observer = observer

	def receive(self, inventory:list[Item])->None:
		for item in inventory:
			#other receiving functions
			self.notify_item_received(item)

	def notify_item_received(self, item:Item)->None:
		self.observer.notify(Event[Item](item.name, item))

class Customer:
	def __init__(self, name:str):
		self.name = name
		
	def get_widget(self, item:Item):
		print('Hey! my widget Arrived!!!')
	

class Store:
	def __init__(self, observer:ObserverInterface, inventoryManager:InventoryManagerInterface):
		self.observer:ObserverInterface = observer
		self.inventoryManager:InventoryManager  = inventoryManager

	def receive_inventory(self, inventory:list[Item])->None:
		#do other receiving stuff
		self.inventoryManager.receive(inventory)

	def subscribe_customer_to_item(self, subscriber:Callable, item:Item):
		def func (data) : 
			subscriber(data)
			self.observer.unsubscribe(func, item.name)
		self.observer.subscribe(func, item.name)

	

def main():
	observer:Observer = Observer()
	jake:Customer = Customer('Jake')
	inventoryManager:InventoryManager = InventoryManager(observer)
	store:Store = Store(observer, inventoryManager)
	store.subscribe_customer_to_item(jake.get_widget, Item(ItemEnum.WIDGET))

	inventory1 = [Item(ItemEnum.HAMMER), Item(ItemEnum.BASEBALL), Item(ItemEnum.CHEESE)]
	inventory2 = [Item(ItemEnum.ROPE), Item(ItemEnum.CHEESE), Item(ItemEnum.WIDGET)]
	store.receive_inventory(inventory1)
	store.receive_inventory(inventory2)
	store.receive_inventory(inventory2)
	

	


if __name__ == "__main__":
	main()