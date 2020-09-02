import socket
import sys
 
host = ""
port = 1234
waterLevel = []
Temperature = []
humidtiy = []

mySocket = socket.socket()
mySocket.bind((host,port))                    # Bind to localhost:1234
     
mySocket.listen(1)                            # Wait for a connection
while True:
    print("Listening...")
    while True:
        conn, addr = mySocket.accept()                # If new connection receives, return conn obj
        #print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()               # Receive data (buffer size 1024 bytes)
        #print ("Received Data is: " + str(data))
        data2 = data.split(":")
        if data2[0] == 'water':
            valueW = int(data2[1])
            waterLevel.insert(0, valueW)
            #avgW = sum(waterList) / len(waterList)
            #print avgW
            #customWrite(0, avgW)
            print("water levle: ")
            print (waterLevel)
        elif data2[0] == 'temp':
            valueT = int(data2[1])
            Temperature.insert(0, valueT)
            #avgW = sum(waterList) / len(waterList)
            #print avgW
            #customWrite(0, avgW)
            print("Temperature: ")
            print (Temperature)
        elif data2[0] == 'humidity':
            valueH = int(data2[1])
            humidtiy.insert(0, valueH)
            #avgW = sum(waterList) / len(waterList)
            #print avgW
            #customWrite(0, avgW)
            print("Humidity: ")
            print (humidtiy)
        elif str(data) == "quit":
            conn.close()
            break;
        #result = int(data)*2                          # Do your processing of incoming data here
        #print ("Sending Results: " + str(result))
        #conn.send(str(result).encode())               # Send data back.
    conn.close()                                  # Close connection
    sys.exit()
