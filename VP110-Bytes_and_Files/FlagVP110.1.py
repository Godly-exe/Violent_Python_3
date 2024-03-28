"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP110.htm
"""

# Download this file:
# https://samsclass.info/124/proj14/VP110-1
# Count the number of '\x08' bytes. That's the flag.

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


# Validate URL
url = 'https://samsclass.info/124/proj14/VP110-1'
check_url(url)

# Download the file
response = requests.get(url)
open('VP110-1', 'wb').write(response.content)

# Validate file exists, get size
if exists('VP110-1'):
    file_size = os.path.getsize('VP110-1')
    print(f"File 'VP110-1' downloaded, size {file_size} bytes")

# Count the number of '\x08' bytes
counter = 0
# Read the file one byte at a time
print("Reading 'VP110-1'")
with open('VP110-1', 'rb') as f:
    byte = f.read(1)
    if byte == b'\x08':
        counter += 1
    while byte != b"":
        # print(byte)
        byte = f.read(1)
        if byte == b'\x08':
            counter += 1

print(f"The number of x08 bytes is {counter}")  # 32
f.close()