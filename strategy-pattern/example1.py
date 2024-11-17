from typing import TypeVar
T = TypeVar('T')

'''
in the below example we have a very typical set up
where there is a UserService class and it has a depency on
a SqlDatabase class.

This is a pattern you will see all the time where a new 
instance of a dependency is created within the class.
The dependency is either imported or as in this case,
defined somewhere else in the file.

the problem here is that the UserService class is not tightly
coupled with the SqlDatabase class.  Any changes to the
SqlDatabase class will have ramifications in the User
class.  This makes our code brittle and difficult to 
test / debug
'''
class UserDatabaseResponseObject:
	#raw data from the database
	pass

class SqlDatabase:
	def get(self, query:dict, type:T)->list[T]:
		#query the datbase
		return [T]

class UserObject:
	def __init__(self, data: UserDatabaseResponseObject):
		#parse data into UserObject
		pass

class UserService:
	def __init__(self):
		self.db = SqlDatabase()

	def get_users(self)->list[UserObject]:
		users = []
		raw_users = self.db.get({}, UserDatabaseResponseObject)
		for user in raw_users:
			users.append(UserObject(user))

		return users
	
def main():
	service = UserService()
	users = service.get_users()
	print(users)

if __name__ == "__main__":
	main()