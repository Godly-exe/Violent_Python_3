"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP210.htm
"""

import base64

cred = "dumbo:dumbo"
auth = base64.b64encode(cred.encode())
print("Base64-encoded credentials", auth.decode())

# Base64-encoded credentials ZHVtYm86ZHVtYm8=