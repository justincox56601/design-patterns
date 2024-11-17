'''
Since we have used the Strategy pattern to make the 
Order class dependent on the NotifierInterface, it 
is trivial to create other Notifiers and swap them 
out.  In this example, I added a FacebookNotifier
and used that.

Since the Facebook Notifier uses the same NotifierInterface
there is no need to change anything in the Order class
other than to send it a FacebookNotifier during construction
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

class FacebookNotifier(NotifierInterface):
	def notify(self, message:str)->None:
		print('This is an Facebook message: {}'.format(message))

class Order:
	def __init__(self, notifier:NotifierInterface):
		self.notifier = notifier

	def process_order(self)->None:
		#do other order processing stuff
		self.notifier.notify('Your order has been processed')

def main():
	facebook = FacebookNotifier()
	order1 = Order(facebook)
	order1.process_order()

if __name__ == "__main__":
	main()

