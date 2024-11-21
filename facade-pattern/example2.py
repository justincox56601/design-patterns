'''
In this example, we create the Logger class
This is a facade class that will make it much 
easier to use the ColorPrinter class.

The Logger class defines serval methods.
	print() - standard print to the screen
	log() - prints to the screen and logs the message
	error() - prints and logs an error message
	warn() - prints and logs a warning message
	success() - prints a success message
	log() - logs a message to a file

all of these methods make use of the 
ColorPrinter.message() method, but pre-fill many of
values for us.

Now the developer has a much cleaner method to use, 
they don't have to be concernd about whether the message
needs to be logged or not, Nor do they ahve to memorize
what colors go with each message type.

'''
from abc import ABC, abstractmethod

class ColorPrinterInterface(ABC):
	@abstractmethod
	def message(self, color:str, message_type:str, message:str, isLogged:bool)->None:pass

class ColorPrinter:
	def message(self, color:str, message_type:str, message:str, isLogged:bool)->None:
		print("\033[{}{}: {}\033[0m".format( color, message_type, message))
		if isLogged:
			#log timestamp, message_type, and message to log file
			print("This was logged")

class Logger:
	RED = '31m'
	GREEN = '32m'
	YELLOW = '33m'
	BLUE = '34m'
	WHITE = '00m'

	def __init__(self, printer:ColorPrinterInterface):
		self._printer = printer

	def print(self, message):
		self._printer.message(self.WHITE, 'Log', message, False)
	
	def log(self, message):
		self._printer.message(self.WHITE, 'Log', message, True)
	
	def error(self, message):
		self._printer.message(self.RED, 'Error', message, True)
	
	def warn(self, message):
		self._printer.message(self.YELLOW, 'Warn', message, True)
	
	def success(self, message):
		self._printer.message(self.GREEN, 'Success', message, False)


def main():
	printer = ColorPrinter()
	logger = Logger(printer)
	
	logger.print("this is much simpler")
	logger.log("Now we only need to be concerned with the message")
	logger.error("no need to remember color codes")
	logger.warn("No need to remember message types")
	logger.success("Don't have to remember if this was logged or not")

if __name__ == "__main__":
	main()