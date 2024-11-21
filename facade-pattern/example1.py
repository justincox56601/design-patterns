'''
The Facade Pattern is a design pattern that provides a 
simplifed interface to a complex system, library, or 
framework

Take the example below.  For reasons, the ColorPrinter 
class is an imported library, and the whole application
needs to use it.  But looking at its message() method 
we notice a code smell.

The developers of this library didn't make the message()
method very simple.  Everytime we want to use it, we
have to know the color, message type, the actual message,
whether we want it logged or not.  With this many
parameters, it is very prone to developer error, and in 
all reality, all we really wanted to do was print a message

This is where the facade pattern comes in handy
'''

class ColorPrinter:
	RED = '31m'
	GREEN = '32m'
	YELLOW = '33m'
	BLUE = '34m'

	def message(self, color:str, message_type:str, message:str, isLogged:bool)->None:
		print("\033[{}{}: {}\033[0m".format( color, message_type, message))
		if isLogged:
			#log timestamp, message_type, and message to log file
			print("This was logged")

def main():
	printer = ColorPrinter()
	printer.message('31m', "Error", 'Danger Will Robinson', True)
	printer.message('34m', "Log", 'just logging to the terminal', False)
	printer.message('32m', "Log", 'All tests pass', False)

if __name__ == "__main__":
	main()