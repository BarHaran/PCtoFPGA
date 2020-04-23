from tcp_lib import *
import socket

def main():
    # Create a TCP socket at client side
    tcp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_address_port = getAddressPort()
    tcp_client_socket.connect(server_address_port)
    msg = ""
    while ((msg != "quit") and (msg != "exit")):
        print("What is your message?")
        msg = input()
        bytes_to_send = str.encode(msg)
        # Send to server using created TCP socket
        tcp_client_socket.send(bytes_to_send)
        msg_from_server = tcp_client_socket.recv(BUFFER_SIZE)
        print("Message from Server {}".format(msg_from_server[0]))


if __name__ == "__main__":
	main()
