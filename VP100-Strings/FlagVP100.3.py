"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

# Connect to the ad.samsclass.info server on port 10204.
# Combine two numbers as required and send the result.
# You have to get all five answers correct within five seconds to get the flag, covered by a green box in the image below.
# Hint: Only connect once. If you connect five times, you'll always be solving the first challenge, and never see the flag.

import socket

# Input
url = 'ad.samsclass.info'
port = 10204

# Process, output
s = socket.socket()
s.connect((url, port))
for i in range(5):
    print()
    print(f"Loop # {i+1}")
    reply = s.recv(1024).decode()
    print(f"Got reply: '{reply}'")

    # Get the numbers out of string
    operation = reply.split()[0]
    num1 = int(reply.split()[-3])
    num2 = int(reply.split()[-2])
    print(f"The operation is: '{operation}'")
    print(f"The numbers are:  '{num1}', '{num2}'")
    if operation == 'Add':
        response = num1 + num2
    elif operation == 'Subtract':
        response = num1 - num2
    else:
        print(f"Unknown operation '{operation}'")

    print(f"Response       : '{response}'")

    # send response and get next question
    s.send((str(response)+'\n').encode())
    print(s.recv(1024).decode())

# send final response and get flag
s.send('Gimme da flag :)\n'.encode())
print(s.recv(1024).decode())
s.close()
