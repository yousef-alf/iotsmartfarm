import client
from gpio import *
from time import *


def main():
	pinMode(0, IN)
	while True:
		client.send("quit")
		value1 = customRead(0)
		print value1
		client.send("water: "+value1)
		value2 = customRead(1)
		print value2
		client.send("temp: "+value2)
		value3 = customRead(2)
		print value3
		client.send("humidity: "+value3)
		
		sleep(0.5)
		
		
if __name__ == "__main__":
	main()
