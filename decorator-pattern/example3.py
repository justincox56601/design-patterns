'''
This is nice and all, but what if we wanted to 
send more than one notification?  Currently, 
Our system only allows for a single notifier to 
be sent into the Order class.  

Well we have a couple options.  We could create
combination notifiers, like TextAndEmailNotififer.
This could be doable with 2 or 3 different notifiers
but will quickly (exponentially) grow in number as
we add new notifiers.  

And in reality, we want to be able to handle an
inlimited number of notifiers.

The second option is the decorator optoin.
We will create a new class called MultiNotifier
and it will implement the same NotifierInterace. But 
in the constructor, it will take a list of NotifierInterfaces

This will allow us to use it in the same way inside
of the Order class, but now we can add our own
functionality to it.

Now we can loop through all of the other notifiers, and 
call their notify method.  The big thing to notice here
is that we made NO CHANGES to the other classes.  
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

class MultiNotifier(NotifierInterface):
	def __init__(self, notifiers:list[NotifierInterface]):
		self._notifiers = notifiers

	def notify(self, message:str)->None:
		for notifer in self._notifiers:
			notifer.notify(message)

class Order:
	def __init__(self, notifier:NotifierInterface):
		self.notifier = notifier

	def process_order(self)->None:
		#do other order processing stuff
		self.notifier.notify('Your order has been processed')

def main():
	text:TextNotifier = TextNotifier()
	email:EmailNotifier = EmailNotifier()
	facebook:FacebookNotifier = FacebookNotifier()
	multi:MultiNotifier = MultiNotifier([text, email, facebook])
	order1 = Order(multi)
	order1.process_order()

if __name__ == "__main__":
	main()

