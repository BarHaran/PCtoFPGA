# Import the socket library
import socket

buffer_size = 1024

# Get the paramters from the user
###### NEED TO ADD MANY CHECKS #######
print("What is the IP that we will listen to?")
local_ip = input()
print("What is the port?")
local_port = int(input())
server_address_port = (local_ip, local_port)

print("What is your message?")
msg_from_client = input()
bytes_to_send   = str.encode(msg_from_client)

# Create a UDP socket at client side
udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
udp_client_socket.sendto(bytes_to_send, server_address_port)

msg_from_server = udp_client_socket.recvfrom(buffer_size)
msg = "Message from Server {}".format(msg_from_server[0])
print(msg)
