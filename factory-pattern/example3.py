from abc import ABC, abstractmethod

'''
In the previous example we decoupled the EmailNotification
class from the Order class.  Now the Order class has a
dependency on the NotificationInterface.  

Now we can use ANY notification class as long as it implements
the NotificationInterface.  This example shows use creating the 
SmsNotification and using that instead of the EmailNotification

The big thing to notice here is that we DID NOT CHANGE anything
about the order class.  We simply created a different Notification
class and instered that as the dependency.
'''

class NotificationInterface(ABC):
	@abstractmethod
	def send(self, message:str)->None:
		pass

class EmailNotification(NotificationInterface):
	def send(self, message:str)->None:
		print('sent from Email: {}'.format(message))

class SmsNotification(NotificationInterface):
	def send(self, message:str)->None:
		print('sent from SMS: {}'.format(message))


class User:
	pass

class Order:
	def __init__(self, user:User, notification:NotificationInterface):
		self.user = user
		self.notification = notification

	def notify_user(self, message)->None:
		self.notification.send(message)

def main():
	user = User()
	notification = SmsNotification()
	order = Order(user, notification)
	order.notify_user("Your order has been shipped")

if __name__ == "__main__":
	main()