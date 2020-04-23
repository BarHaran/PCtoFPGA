# Import the socket library
import socket

BUFFER_SIZE = 1024

# Get the paramters from the user
###### NEED TO ADD MANY CHECKS #######
def getAddressPort():
   ##### Add script argument for getting the ip and port, enforcing int ##### 
	print("Enter the server's ip:")
	local_ip = input()
	print("What is the port?")
	local_port = int(input())
	return (local_ip, local_port)

def main():
    # Create a UDP socket at client side
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server_address_port = getAddressPort()
    msg = ""
    while (msg != "quit" | msg != "exit"):
        print("What is your message?")
        msg = input()
        bytes_to_send   = str.encode(msg)
        # Send to server using created UDP socket
        udp_client_socket.sendto(bytes_to_send, server_address_port)
        msg_from_server = udp_client_socket.recvfrom(BUFFER_SIZE)
        print("Message from Server {}".format(msg_from_server[0]))