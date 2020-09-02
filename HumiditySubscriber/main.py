import mqttclient
from time import *
from gpio import *

pinMode(0, OUTPUT)

broker_add ='192.168.0.100'						#Broker Address
username= 'user1'								#Username
password = '1234'								#Password
sub3 = 'humidity'									#Subscription topic




def on_connect(status, msg, packet):			#show connection status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	
def on_disconnect(status, msg, packet):			#show disconnection status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	

def on_subscribe(status, msg, packet):			#show subscription status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	

def on_unsubscribe(status, msg, packet):		#show unsubscription status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	

def on_publish(status, msg, packet):			#show publishing status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	
def on_message_received(status, msg, packet):  #Invoked when new message received
	# check received message and take action
	if status == "Success" or status == "Error":
		print status + ": " + msg
	
	elif status == "":
		humidityR = int(msg)
		print humidityR
		if humidityR > 70:
			customWrite(0, "2")
			print humidityR
		elif humidityR > 60:
			customWrite(0, "1")
			print humidityR
		elif humidityR < 60:
			customWrite(0,"0")
		#if msg
		"""
		if msg == "heat":
			digitalWrite(0, HIGH)
		elif msg == "dont":
			digitalWrite(0, LOW)
		"""
		#print tempR
		
	
def main():
	
	mqttclient.init()

	mqttclient.onConnect(on_connect)
	mqttclient.onDisconnect(on_disconnect)
	mqttclient.onSubscribe(on_subscribe)
	mqttclient.onUnsubscribe(on_unsubscribe)
	mqttclient.onPublish(on_publish)
	mqttclient.onMessageReceived(on_message_received)
	print('Client Initialized')

	mqttclient.connect(broker_add,username,password)
	while not mqttclient.state()["connected"]:		#wait until connected
 		pass											#do nothing
 
	mqttclient.subscribe(sub3)

	while True:
		delay(1000);
		
if __name__ == "__main__":
	main()
