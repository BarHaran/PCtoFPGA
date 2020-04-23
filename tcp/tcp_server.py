from tcp_lib import *
import socket

def main():
        # The DGRAM socket corresponds to the tcp
        tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # Get ip and port
        local_ip, local_port = getAddressPort()

        # Bind to address and ip
        tcp_server_socket.bind((local_ip, local_port))
        tcp_server_socket.listen(1)
        print("tcp server up and listening")

        message = b""
        conn, addr = tcp_server_socket.accept()

        print("Got connection from {}".format(addr))

        # Listen for incoming messages until given exit signal
        while(message != b"exit"):
                # Recieve data from the tcp connection
                message = conn.recv(BUFFER_SIZE)

                # Sending a reply depending on the message
                if(message == b"quit"):
                        conn.send(b"Goodbye")
                elif (message == b"exit"):
                        conn.send(b"Server shutting down")
                else:
                        conn.send(b"Server got your message")


if __name__ == "__main__":
        main()
