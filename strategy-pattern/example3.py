from abc import ABC, abstractmethod
from typing import TypeVar
T = TypeVar('T')

'''
We still have one last step.  Currently we have 
decoupled the UserService from the creation of the 
SqlDatabase class.  But we are still dependent on
the specific SqlDatabase class.

What would happen if in the future we wanted to
switch to a document database like MongoDb?  we would
have to find every class that has a dependency on the
SqlDatabase class and not only update that dependency, 
but also potentially change the class code to interact
with the new database class.

Instead what we want to do is create a DatabaseInterface
This will define that every class implementing this
interface will have at least teh methods defined in the 
interface.  

(A class implementing multiple interfaces is common)

Then we will make the UserService dependent on the 
DatabaseInterface.  In this way, as long as we provide
it with a class that implements the DatabaseInterface
we will not have to worry about changing any code inside
of the UserService.

All class depencies should be interfaces, Not concrete 
implementations.  This allows us to hot swap them any
time we need to.  Including during runtime.
'''

class UserDatabaseResponseObject:
	#raw data from the database
	pass

class DatabaseInterface(ABC):
	@abstractmethod
	def get(self, query:dict, type:T)->list[T]:pass

class SqlDatabase(DatabaseInterface):
	def get(self, query:dict, type:T)->list[T]:
		#query the datbase
		return [T]

class MongoDatabase(DatabaseInterface):
	def get(self, query:dict, type:T)->list[T]:
		#query the document database
		return [T]

class UserObject:
	def __init__(self, data: UserDatabaseResponseObject):
		#parse data into UserObject
		pass

class UserService:
	def __init__(self, database:DatabaseInterface):
		self.db = database

	def get_users(self)->list[UserObject]:
		users = []
		raw_users = self.db.get({}, UserDatabaseResponseObject)
		for user in raw_users:
			users.append(UserObject(user))

		return users
	
def main():
	sql = SqlDatabase()
	service1 = UserService(sql)
	users1 = service1.get_users()
	print(users1)

	mongo = MongoDatabase()
	service2 = UserService(mongo)
	users2 = service2.get_users()
	print(users2)

if __name__ == "__main__":
	main()