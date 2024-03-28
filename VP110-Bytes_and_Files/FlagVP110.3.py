"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP110.htm
"""

# Download these two files:
# https://samsclass.info/124/proj14/VP110-3a
# https://samsclass.info/124/proj14/VP110-3b
# Add the bytes in the two files together to construct a new file named VP110-3-flag.png.
# Open that file in an image viewer to see the flag.

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
url1 = 'https://samsclass.info/124/proj14/VP110-3a'
url2 = 'https://samsclass.info/124/proj14/VP110-3b'

# Check URLs
check_url(url1)
check_url(url2)

# Download the files
response = requests.get(url1)
open('VP110-3a', 'wb').write(response.content)
response = requests.get(url2)
open('VP110-3b', 'wb').write(response.content)

# Validate file exists, get size
if exists('VP110-3a'):
    file_size = os.path.getsize('VP110-3a')
    print(f"File 'VP110-3a' downloaded, size {file_size} bytes")
    # File 'VP110-3a' downloaded, size 38094 bytes
if exists('VP110-3b'):
    file_size = os.path.getsize('VP110-3b')
    print(f"File 'VP110-3b' downloaded, size {file_size} bytes")
    # File 'VP110-3b' downloaded, size 38094 bytes

# Adding the bytes in the two files together to construct a new file named VP110-3-flag.png
with open('VP110-3a', 'rb') as f:
    with open('VP110-3b', 'rb') as g:
        with open('VP110-3-flag.png', 'wb') as h:
            for i in range(file_size):
                byte1 = f.read(1)
                byte2 = g.read(1)
                combined = byte1[0] + byte2[0]
                h.write(bytes([combined]))

# Validate new file size
if exists('VP110-3-flag.png'):
    file_size = os.path.getsize('VP110-3-flag.png')
    print(f"File 'VP110-3-flag.png' validated, size {file_size} bytes")
    # File 'VP110-3-flag.png' validated, size 38094 bytes
    # s0_1337

f.close()
g.close()
h.close()
