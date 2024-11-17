from abc import ABC, abstractmethod
from enum import Enum

'''
Currently we are able to create any number of notifications
and use them as we see fit.  But what if we didn't know 
which notification we wanted to send?

What if we have made the business decision to allow the user
to pick their notification preference?

In this scenario, we can't know during development which
one the user will pick.  So how can we send in the notification
dependency?

One way, the naive way, is to use a switch statement.  This example 
shows one way that could be implemented.

There are several problems with this method though.  Even though it 
works in small cases, it will be difficult to maintain.  Everytime 
we decided to add or remove a notification, we will have to find its
usage in the Order class and update the Order class. 

That should be raising read flags in your head.  Why should we update
the Order class when we are making changes to the Notifications? And 
what happens when this gets implemented in more than just the Order 
class?  This creates code duplication, is prone to errors, and makes
our software brittle.

Basically we have just recoupled the creation logic of the notifications
with the Order class again.
'''

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

class User:
	def __init__(self):
		#other config properties...
		self.notification_preference = NotificationPreferenceEnum.SMS

class Order:
	def __init__(self, user:User):
		self.user = user

	def notify_user(self, message)->None:
		if self.user.notification_preference == NotificationPreferenceEnum.EMAIL:
			notification = EmailNotification()
			notification.send(message)
		elif self.user.notification_preference == NotificationPreferenceEnum.SMS:
			notification = SmsNotification()
			notification.send(message)
		elif self.user.notification_preference == NotificationPreferenceEnum.PUSH:
			notification = PushNotification()
			notification.send(message)

def main():
	user = User()
	order = Order(user)
	order.notify_user("Your order has been shipped")

if __name__ == "__main__":
	main()