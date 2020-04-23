from udp_lib import *

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
                print("Message from Client:{}".format(message))
                print("Client IP Address:{}".format(address))
                # Sending a reply depending on the message
                if(message == b"quit"):
                        udp_server_socket.sendto(b"Goodbye", address)
                elif (message == b"exit"):
                        udp_server_socket.sendto(b"Server shutting down", address)
                else:
                        udp_server_socket.sendto(b"Server got your message", address)


if __name__ == "__main__":
        main()
