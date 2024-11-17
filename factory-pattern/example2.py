from abc import ABC, abstractmethod

'''
In the previous example the send_notification method
and by extension the Order class are tightly coupled
with the EmailNotification class.  

Here we create a proper notification interface and
make it a dependency of the Order class.  This will
decouple the order class from email notifications
'''

class NotificationInterface(ABC):
	@abstractmethod
	def send(self, message:str)->None:
		pass

class EmailNotification(NotificationInterface):
	def send(self, message:str)->None:
		print('sent from Email: {}'.format(message))


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
	notification = EmailNotification()
	order = Order(user, notification)
	order.notify_user("Your order has been shipped")

if __name__ == "__main__":
	main()