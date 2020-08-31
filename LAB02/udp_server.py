# UDP SERVER CODE
# This server gets an utf-8 string from a client and converts it in all caps

# Import everything from the socket library
from socket import *

# We specify the port the server will be listening at
serverPort = 42069

# We now open a socket. When the process starts, opens a socket.
# We pass two parameters to the socket function. We specify:
#   AF_INET: use IPv4 (otherwise one could use AF_INET6 to use IPv6)
#   SOCK_DGRAM: use UDP (otherwise one could use SOCK_STREAM to use TCP)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# We now need to bind the socket to a specified address, we do not specify the host name but we specify the port
# The address has form (name, port)
serverSocket.bind( ('',serverPort) )

print("Server running\n")

# The server will continue running
while 1:
    # We now read from a socket, we specify 2048 buffer size.
    message, clientAddress = serverSocket.recvfrom(2048)

    # UTF-8 decode
    message = message.decode('utf-8')

    # Print what we got
    print("From client: ", clientAddress)
    print("Received message: ",message,'\n')

    # Convert to upper case
    responseMessage = message.upper()

    # We now send back the response to clientAddress
    serverSocket.sendto(responseMessage.encode('utf-8'),clientAddress)


