from abc import ABC, abstractmethod
from enum import Enum
from typing import List

'''
In the final example, we are now faced with the problem of
having more than 1 notification method.  The powers that be
have decided to allows the users to have more than one notification
preference.  

Luckily for us, we have put ourself in a good position, so that we
can make this happen fairly easily by combining the factory pattern
with the decorator pattern.

first since we are changing the data assicated with the user, we
need to update our UserObject.  We are going to add a field called
notification_preferences.  This will be an array of enums.  NOTICE
we are not removing the old preference or changing it.  That may 
be used in other pieces of code, and we are not refactoring at this 
moment.

second we want to create a new Notification.  Since we are already
using the NotificationInterface in our Orders class, we will want
to keep using it.  MultiNotification will implement the 
NotificationInterface so that we can still use the same interface
methods we have already been using.  It will also take in a list
of NotificationInterfaces in it's constructor.  Then the send() 
method will simply loop over that list and call the send() method
of each notification.

Third, since we have a new Notification that uses a different 
constructor than the previous ones, we will need to create a 
new factory for it.

Finally, notice how once we created the new MultiNotification 
and the new MultiNotificationFactory.  The only change we needed
to make in the main() function, was to change the 
NotificationFactory to MulitNotificationFactory and everything 
worked the same
'''
class User:
	def __init__(self):
		#other config properties...
		self.notification_preference = NotificationPreferenceEnum.SMS
		self.notification_preferences = [
			NotificationPreferenceEnum.SMS,
			NotificationPreferenceEnum.PUSH,
			NotificationPreferenceEnum.EMAIL
		]
		
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

class MultiNotificaiton(NotificationInterface):
	def __init__(self, notifications:List[NotificationInterface]):
		self.notifications = notifications

	def send(self, message)->None:
		for notification in self.notifications:
			notification.send(message)

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
		
class MultiNotificationFactory(NotificationFactoryInterface):
	def create(self, user:User)->NotificationInterface:
		notifications = []
		for preference in user.notification_preferences:
			if preference == NotificationPreferenceEnum.EMAIL:
				notifications.append(EmailNotification())
			if preference == NotificationPreferenceEnum.SMS:
				notifications.append(SmsNotification())
			if preference == NotificationPreferenceEnum.PUSH:
				notifications.append(PushNotification())

		return MultiNotificaiton(notifications)

class Order:
	def __init__(self, user:User, notificationFactory:NotificationFactoryInterface):
		self.user = user
		self.notification = notificationFactory.create(self.user)

	def notify_user(self, message)->None:
		self.notification.send(message)

def main():
	user = User()
	notificationFactory = MultiNotificationFactory()
	order = Order(user, notificationFactory)
	order.notify_user("Your order has been shipped")

if __name__ == "__main__":
	main()