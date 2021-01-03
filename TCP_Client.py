import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.10.155.42', 42000)
print(('\nConnecting to port: ' + str(server_address)) + '\n')
print('I am the client')

#sock.connect(server_address)
sock.connect(server_address)
i = 0
carrierval = 0
stationval = 0

message1 = """<PLC>
    <RFID>
        <CarrierID>"""
message2 = """</CarrierID>
        <StationID>"""
message3 = """</StationID>
        <DateTime>"""
message4 = """</DateTime>
    </RFID>
</PLC>"""

for i in range(16):
    carrierval = i + 1
    print (str(i))
    print (str(carrierval))
    for j in range(16):
        localtime = time.asctime(time.localtime(time.time()))
        stationval =  j + 1
        message = message1 + str(carrierval) + message2 + str(stationval) + message3 + localtime + message4
        print('Sending: \n' + message + '\n')
        sock.sendall(message.encode())
        time.sleep(0.5)
        data2 = sock.recv(1024)
        strings = str(data2, 'utf8')
        num = int(strings)
        remain_t = num/1000 -0.5
        print ('Remaining wait time in seconds :' + str(remain_t))
        time.sleep(remain_t)
