'''
the decorator pattern is a behavioral pattern where
we wrap the behavior of one class inside of another
class.

Think of anytime you want to create a wrapper around
an object that allows you to use the same functionality
as the original object, but extend it with your own.

In the example below we have a simple notificationInterface 
that defines the notify method.  Then we have two concrete
notifiers the TextNotifier and the EmailNotifier

when the Order class is instantiated it receives a notifier 
and uses that to notify the customer during the process_order
method.
'''

from abc import ABC, abstractmethod

class NotifierInterface(ABC):
	@abstractmethod
	def notify(self, message:str)->None:pass

class TextNotifier(NotifierInterface):
	def notify(self, message:str)->None:
		print('This is a text message: {}'.format(message))

class EmailNotifier(NotifierInterface):
	def notify(self, message:str)->None:
		print('This is an email: {}'.format(message))

class Order:
	def __init__(self, notifier:NotifierInterface):
		self.notifier = notifier

	def process_order(self)->None:
		#do other order processing stuff
		self.notifier.notify('Your order has been processed')

def main():
	text = TextNotifier()
	order1 = Order(text)
	order1.process_order()

	email = EmailNotifier()
	order2 = Order(email)
	order2.process_order()

if __name__ == "__main__":
	main()

