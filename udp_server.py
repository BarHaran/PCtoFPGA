# Import the socket library
import socket

buffer_size  = 1024

# Get the paramters from the user
###### NEED TO ADD MANY CHECKS #######
print("What is the IP that we will listen to?")
local_ip = input()
print("What is the port?")
local_port = int(input())

# The DGRAM socket corresponds to the UDP
udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
udp_server_socket.bind((local_ip, local_port))

print("UDP server up and listening")

# Listen for incoming DGRAM
while(True):
    bytes_address_pair = udp_server_socket.recvfrom(buffer_size)
    message = bytes_address_pair[0]
    address = bytes_address_pair[1]
    client_msg = "Message from Client:{}".format(message)
    client_ip  = "Client IP Address:{}".format(address)
    print(client_msg)
    print(client_ip)
    # Sending a reply that is equal to what we received to the client
    udp_server_socket.sendto(message, address)
