# Import libraries
import socket

# Constants
BUFFER_SIZE = 1024

# Functions

def valid_ip(ip):
    nums = ip.split('.')
    if len(nums) != 4:
        return False
    for num in nums:
        if not num.isdigit():
            return False
        number = int(num)
        if number < 0 or number > 255:
            return False
    return True

def getAddressPort():
   ''' The function gets an input from the user.
       It gets the ip and the port that is used for the communication. '''
   # Getting the ip
   print("Enter the server's ip:")
   local_ip = input()
   while(not valid_ip(local_ip)):
       print("Please enter a valid ip:")
       local_ip = input()
   
   # Getting the port number
   print("What is the port?")
   local_port = input()
   while(not local_port.isnumeric() or int(local_port) < 1024 or int(local_port) > 65535):
        print("Please enter a valid port number:")
        local_port = input()
   local_port = int(local_port)

   # Return the ip and the port in a tuple
   return (local_ip, local_port)

