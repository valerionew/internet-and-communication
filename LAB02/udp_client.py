# UDP CLIENT CODE
# This cliend sends an user input string via UDP to a server, the server converts it in all caps

# Import everything from the socket library
from socket import *

# We then define IP and port number for the server
# The server will be hosted on localhost, so we rely on the local dns to resolve the name to 127.0.0.1
serverName = 'localhost'
# we pick port 42069
serverPort =  42069

# We now open a socket. When the process starts, opens a socket.
# We pass two parameters to the socket function. We specify:
#   AF_INET: use IPv4 (otherwise one could use AF_INET6 to use IPv6)
#   SOCK_DGRAM: use UDP (otherwise one could use SOCK_STREAM to use TCP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# User input
message = input('Insert a string to be converted to caps by our server\n')

# We now send the data to the server
# We need to encode the message in utf-8
# Then we specify the tuple (name, port) for the server
clientSocket.sendto(message.encode(encoding='utf-8'), (serverName,serverPort))

# If the server is unreachable, we time out after 1 second of no response
clientSocket.settimeout(1) # In seconds

# We catch the timeout exception
try:
    # We now wait for the response from the server. We need to specify the max buffer size for the receive buffer. We pick:
    #      2048
    responseMessage, serverAddress = clientSocket.recvfrom(2048)

    # It is time to present the response we got fromthe server
    responseMessage = responseMessage.decode('utf-8')
    print("The string is: ", responseMessage)

# This is what we do if there's an exception
except timeout:
    # We show an error message
    print("TIMEOUT - server unreachable")

# This is what is done in either case (eception/no exception)
finally:
    # We now close the socket
    clientSocket.close()
