from tcp_lib import *
import socket

def main():
        # The DGRAM socket corresponds to the tcp
        tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # Get ip and port
        local_ip, local_port = getAddressPort()

        # Bind to address and ip
        tcp_server_socket.bind((local_ip, local_port))
        print("tcp server up and listening")

        message = b""

        # Listen for incoming messages until given exit signal
        while(message != b"exit"):
                bytes_address_pair = tcp_server_socket.recvfrom(BUFFER_SIZE)
                message = bytes_address_pair[0]
                address = bytes_address_pair[1]
                print("Message from Client:{}".format(message))
                print("Client IP Address:{}".format(address))
                # Sending a reply depending on the message
                if(message == b"quit"):
                        tcp_server_socket.sendto(b"Goodbye", address)
                elif (message == b"exit"):
                        tcp_server_socket.sendto(b"Server shutting down", address)
                else:
                        tcp_server_socket.sendto(b"Server got your message", address)


if __name__ == "__main__":
        main()
