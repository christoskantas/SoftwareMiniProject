import socket
import sys
import time
import xml.etree.ElementTree as ET
import csv

# Create a TCP/IP socket
tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.10.155.42', 42000)

#print >>sys.stderr, 'starting up on %s port %s' % server_address
print('\nStarting up on port: ' + str(server_address) + '\n')
tcpserver.bind(server_address)
tcpserver.listen(1)
# Listen for incoming connections
#tcpserver.listen(1)

# Wait for a connection
print('Waiting for a connection..')
print('I am the server')

connection, client_address = tcpserver.accept()
i = 0

while i<256:
    #print('Sending: \n' + message + '\n')
    data = connection.recv(1024)
    #connection.sendall(message.encode())
    print (i)
    xmlstring = data.decode() 
    print('Receivced: \n' + xmlstring)
    if data:
                #startTime = time.perf_counter()

                parser = ET.XMLParser(encoding="utf-8")
                root = ET.fromstring(xmlstring, parser=parser)
                print('\nParsed: ' + str(root))
                            
                CarrierID = int(root[0][0].text)
                print('CarrierID: ' + str(CarrierID))
                
                StationID = int(root[0][1].text)
                print('StationID: ' + str(StationID))
                
                DateTime = str(root[0][2].text)
                print('Date and Time: ' + DateTime)
    if i ==0:
       with open('C:/Users/mar/Desktop/storeddata.csv', 'w') as stored_data:
                    csv_writer = csv.writer(stored_data, delimiter=';')
                    csv_writer.writerow([CarrierID,StationID,DateTime])
    else: 
       with open('C:/Users/mar/Desktop/storeddata.csv', 'a') as stored_data:
                    csv_writer = csv.writer(stored_data, delimiter=';')
                    csv_writer.writerow([CarrierID,StationID,DateTime])

    with open('C:/Users/mar/Desktop/lmao/procssing_times_table.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == CarrierID:
                estPrcsTime = row[StationID]
                connection.sendall(estPrcsTime.encode())
                print('\nEstimated Proccesing Time: ' + str(estPrcsTime) + ' ms')
            line_count += 1
    i += 1
