# Import the socket library
import socket

local_ip     = "127.0.0.1"
local_port   = 20001
buffer_size  = 1024

server_msg    = "Hello World"
bytes_to_send = str.encode(server_msg)

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
    # Sending a reply to client
    udp_server_socket.sendto(bytes_to_send, address)
