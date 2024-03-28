"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

import socket

# Create a socket object named "s"
s = socket.socket()  # type(s) ==> <class 'socket.socket'>

# Connect to the server "ad.samsclass.info" on port 10201
s.connect(("ad.samsclass.info", 10201))

# Receive data from the server, up to a maximum of 1024 characters
mybytes = s.recv(1024)  # type(bytes) ==> <class 'bytes'>

# decode the raw data
decoded_bytes = mybytes.decode()  # type(decoded_bytes) ==> <class 'str'>

# Print the received data to the console
print(decoded_bytes)

# Encode and send a message back to the API/listener
s.send("Hello from INF601!\n".encode())

# Receive, decode, and print the received data
print(s.recv(1024).decode())

# Close the socket
s.close()
