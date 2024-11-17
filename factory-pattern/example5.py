from abc import ABC, abstractmethod
from enum import Enum

'''
In situations like this where we have a dependency but we don't
know until runtime which dependency we will need, we look at
using the factory pattern.

The factory pattern takes on the responsibility of creatiion
so that we can again decouple the notifications from the Order
class.  We still need to in this case use a switch statement
to determine which Notification to create, but now it is
isolated to just the one class where it belongs.

Additionally, anytime I want to create a new Notification, 
all I need to do is create it, add it to the enum, and add 
it to the factory.

Here I created a NotificationFactoryInterface.  Since we are 
only implementing the 1 NotificaitonFactory we could get away
with not using it.  But as we will see in future examples
the proper way to handle it (well all dependencies really) is 
to use an interface.  This makes the Order class depenedent on
the interface, not any one implementation of it.
'''
class User:
	def __init__(self):
		#other config properties...
		self.notification_preference = NotificationPreferenceEnum.SMS
		
class NotificationPreferenceEnum(Enum):
	EMAIL = 'EMAIL'
	SMS = 'SMS'
	PUSH = 'PUSH'

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

class PushNotification(NotificationInterface):
	def send(self, message:str)->None:
		print('sent from Push: {}'.format(message))

class NotificationFactoryInterface(ABC):
	def create(self, type:NotificationPreferenceEnum)->NotificationInterface:
		pass

class NotificationFactory(NotificationFactoryInterface):
	def create(self, user:User)->NotificationInterface:
		type = user.notification_preference
		if type == NotificationPreferenceEnum.EMAIL:
			return EmailNotification()
		elif type == NotificationPreferenceEnum.SMS:
			return SmsNotification()
		elif type == NotificationPreferenceEnum.PUSH:
			return PushNotification()
		


class Order:
	def __init__(self, user:User, notifationFactory:NotificationFactoryInterface):
		self.user = user
		self.notificationFactory = notifationFactory

	def notify_user(self, message)->None:
		notification = self.notificationFactory.create(self.user)
		notification.send(message)

def main():
	user = User()
	notificationFactory = NotificationFactory()
	order = Order(user, notificationFactory)
	order.notify_user("Your order has been shipped")

if __name__ == "__main__":
	main()