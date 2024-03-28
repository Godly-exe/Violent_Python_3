"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP110.htm
"""

# Download these two files:
# https://samsclass.info/124/proj14/VP110-2a
# https://samsclass.info/124/proj14/VP110-2b
# Add the bytes in the two files together to construct the flag.
# For example, if the first file contains b'\x40' and the second contains b'\x01', the result is b'\x41', or "A".

import requests
from os.path import exists
import os


def check_url(url):
    try:
        get = requests.get(url)
        if get.status_code == 200:
            return f"{url}: is reachable"
        else:
            return f"{url}: is Not reachable, status_code: {get.status_code}"

    except requests.exceptions.RequestException as e:
        raise SystemExit(f"{url}: is Not reachable \nError details: {e}")

# Input
url1 = 'https://samsclass.info/124/proj14/VP110-2a'
url2 = 'https://samsclass.info/124/proj14/VP110-2b'

# Check URLs
check_url(url1)
check_url(url2)

# Download the files
response = requests.get(url1)
open('VP110-2a', 'wb').write(response.content)
response = requests.get(url2)
open('VP110-2b', 'wb').write(response.content)

# Validate file exists, get size
if exists('VP110-2a'):
    file_size = os.path.getsize('VP110-2a')
    print(f"File 'VP110-2a' downloaded, size {file_size} bytes")
    # File 'VP110-2a' downloaded, size 24 bytes
if exists('VP110-2b'):
    file_size = os.path.getsize('VP110-2b')
    print(f"File 'VP110-2b' downloaded, size {file_size} bytes")
    # File 'VP110-2b' downloaded, size 24 bytes

# Adding the bytes in the two files
my_flag = ''
with open('VP110-2a', 'rb') as f:
    with open('VP110-2b', 'rb') as g:
        for i in range(file_size):
            byte1 = f.read(1)
            byte2 = g.read(1)
            combined = byte1[0] + byte2[0]
            my_flag += bytes([combined]).decode()

print(my_flag)  # The flag is ADDING_BYTES

f.close()
g.close()
