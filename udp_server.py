# Import the socket library
import socket

# Constants
BUFFER_SIZE  = 1024


# Function gets the ip address from the machine, needs to be given a port manually
def getAddressPort():
	##### Add script argument for getting the ip and port, enforcing int ##### 
	print("Input the server's ip:")
	local_ip = input()
	print("What is the port?")
	local_port = int(input())
	return [local_ip, local_port]


def main():
	# The DGRAM socket corresponds to the UDP
	udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	# Get ip and port
	local_ip, local_port = getAddressPort()

	# Bind to address and ip
	udp_server_socket.bind((local_ip, local_port))
	print("UDP server up and listening")

	message = b""

	# Listen for incoming DGRAM until given exit signal
	while(message != b"exit"):
	    bytes_address_pair = udp_server_socket.recvfrom(BUFFER_SIZE)
	    message = bytes_address_pair[0]
	    address = bytes_address_pair[1]
	    client_msg = "Message from Client:{}".format(message)
	    client_ip  = "Client IP Address:{}".format(address)
	    print(client_msg)
	    print(client_ip)
	    # Sending a reply that is equal to what we received to the client
	    udp_server_socket.sendto(message, address)


if __name__ == "__main__":
	main()