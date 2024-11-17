
'''
The factory pattern is a creation desugn pattern used for
separating creation logic from business logic
'''

'''
Scenario, we have an ecommerce store.  inside of that
store we have an Order class.  It is responsible for 
several things, including notifying the customer at 
different times, such as order placed, order shipped, 
etc...
'''

'''
Beginning Example:
Here we have a simple set up, we only have the
EmailNotificaiton class, so we create a new instance of it
and send the email when we need to notify the customer
'''
class User:
	pass

class EmailNotification:
	def send(self, message:str)->None:
		print('sent from Email: {}'.format(message))



class Order:
	def __init__(self, user:User):
		pass
	
	#do stuff....
	
	def notify_user(self, message)->None:
		notification = EmailNotification()
		notification.send(message)


def main():
	user = User()
	order = Order(user)
	order.notify_user("Your order has been shipped")

if __name__ == "__main__":
	main()