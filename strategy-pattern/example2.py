from typing import TypeVar
T = TypeVar('T')

'''
In order to decouple the UserService from the 
SqlDatabase class, we will perform what is called
dependency injection.  

This is where, instead of creating a new instance
of the SqlDatabase class inside of the UserService
class, we off load the repsonsibility of creation 
to somone else, and have the service itelf passed
in as a paramter during construction
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
	def __init__(self, database:SqlDatabase):
		self.db = database

	def get_users(self)->list[UserObject]:
		users = []
		raw_users = self.db.get({}, UserDatabaseResponseObject)
		for user in raw_users:
			users.append(UserObject(user))

		return users
	
def main():
	database = SqlDatabase()
	service = UserService(database)
	users = service.get_users()
	print(users)

if __name__ == "__main__":
	main()