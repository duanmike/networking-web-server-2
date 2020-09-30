#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    serverSocket.bind(('',13331))
    serverSocket.listen(1)
    print('The server is ready to receive')
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message =  connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            #Send one HTTP header line into socket
            #Fill in start
            header = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n'
            connectionSocket.send(header.encode())
            #Fill in end 

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send('HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\n\r\n'.encode())
            #Fill in end 

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
