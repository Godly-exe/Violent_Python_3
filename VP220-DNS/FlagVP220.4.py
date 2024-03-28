

# In a Web browser, open this page:
# https://samsclass.info/124/proj14/VP220-4.php
# Monitor the DNS requests. Some of the requests are different from the others, and they contain the flag.
# Hints
# Write a script that prints out only the server names, as shown below.
# Find the names that are different and remove all the others.
# You can open multiple copies of the page to get more requests faster.
# Compare the special server names.

from scapy.all import *
import sys

def findDNS(p):
    if p.haslayer(DNS):
        msg = p[DNS].summary()
        if 'samsclass.info' in msg:
            server_name = str(msg).split('"')[1].split('.')[0].split("'")[1]
            if len(server_name) != 50:
                return server_name

print("Listening on DNS traffic for 'different samsclass.info' server names!?")
sniff(prn=findDNS)

sys.exit()

# The majority of server names were 50 characters long. Few were 49:
server_list = [
    'fofwvfdh1jzuogdxdesreverxsixgalfxzuogdhpmwb6ksbqg',
    'fofwvfdh1jzuogdxdesreverxsixgalfxzuogdhpmwb6ksbqg',
    'guydjdpm8whhkjcxdesreverxsixgalfxhhkjcq76w3c579ry',
    'guydjdpm8whhkjcxdesreverxsixgalfxhhkjcq76w3c579ry',
    'dosbxbyyumuqxcyxdesreverxsixgalfxuqxcy6jgp9zre99k',
    'dosbxbyyumuqxcyxdesreverxsixgalfxuqxcy6jgp9zre99k',
    'q4acnpics8bmf5pxdesreverxsixgalfxbmf5pdgkuyf6dcsf',
    'q4acnpics8bmf5pxdesreverxsixgalfxbmf5pdgkuyf6dcsf',
    'o8dc1zoyy0m6b8cxdesreverxsixgalfxm6b8cfzdk5wdkdnn',
    'o8dc1zoyy0m6b8cxdesreverxsixgalfxm6b8cfzdk5wdkdnn',
    'lb5nplr5bkt9iz5xdesreverxsixgalfxt9iz5qke4nwylqmp',
    'lb5nplr5bkt9iz5xdesreverxsixgalfxt9iz5qke4nwylqmp',
    'vh6vmfeu9smfuegxdesreverxsixgalfxmfuegnetbukgcmd7',
    'vh6vmfeu9smfuegxdesreverxsixgalfxmfuegnetbukgcmd7',
    'rq0eumwui6i9swsxdesreverxsixgalfxi9swsfh9hcvldszk',
    'rq0eumwui6i9swsxdesreverxsixgalfxi9swsfh9hcvldszk',
    'uqc69xsmo0w1sztxdesreverxsixgalfxw1szti1zqkwwfoer',
    'uqc69xsmo0w1sztxdesreverxsixgalfxw1szti1zqkwwfoer',
    'fkt6nywcxnumwrhxdesreverxsixgalfxumwrhlmvgakmdqyu',
    'fkt6nywcxnumwrhxdesreverxsixgalfxumwrhlmvgakmdqyu',
    'gqmw7egszk8ygfcxdesreverxsixgalfx8ygfc6j4lbhbgm1v',
    'gqmw7egszk8ygfcxdesreverxsixgalfx8ygfc6j4lbhbgm1v',
    'xoip6wcjzpheohqxdesreverxsixgalfxheohqnpk9d5ouees',
    'xoip6wcjzpheohqxdesreverxsixgalfxheohqnpk9d5ouees',
    'lbwjjdjhk5rbmxuxdesreverxsixgalfxrbmxusulu8u4xwyo',
    'lbwjjdjhk5rbmxuxdesreverxsixgalfxrbmxusulu8u4xwyo',
    'qkqxnfmj02m4cbtxdesreverxsixgalfxm4cbtei7dsmnqrj0',
    'qkqxnfmj02m4cbtxdesreverxsixgalfxm4cbtei7dsmnqrj0',
    'yr2sxosdlvdubhpxdesreverxsixgalfxdubhprlzfmkbvqts',
    'yr2sxosdlvdubhpxdesreverxsixgalfxdubhprlzfmkbvqts',
    'fixivzvd8gtn99yxdesreverxsixgalfxtn99ynvgz9p0nvqy',
    'fixivzvd8gtn99yxdesreverxsixgalfxtn99ynvgz9p0nvqy',
    'fixivzvd8gtn99yxdesreverxsixgalfxtn99ynvgz9p0nvqy',
    'fixivzvd8gtn99yxdesreverxsixgalfxtn99ynvgz9p0nvqy',
    'cmk55gmrbwlczrqxdesreverxsixgalfxlczrqtgzhzbxninf',
    'cmk55gmrbwlczrqxdesreverxsixgalfxlczrqtgzhzbxninf',
    'zxzgnobz4arwqhkxdesreverxsixgalfxrwqhkewtwomvsml5',
    'zxzgnobz4arwqhkxdesreverxsixgalfxrwqhkewtwomvsml5',
    'jdnvs0yjpc6zkayxdesreverxsixgalfx6zkayx5fr3bci0q3',
    'jdnvs0yjpc6zkayxdesreverxsixgalfx6zkayx5fr3bci0q3',
    'akv0ryjoysfgjpfxdesreverxsixgalfxfgjpfegyzitifo73',
    'akv0ryjoysfgjpfxdesreverxsixgalfxfgjpfegyzitifo73',
    'gvcad8ctkmk6nhmxdesreverxsixgalfxk6nhmd53x2zpp4uy',
    'gvcad8ctkmk6nhmxdesreverxsixgalfxk6nhmd53x2zpp4uy',
    'cedfhzgyls5r7yfxdesreverxsixgalfx5r7yfotwkguzx6rk',
    'cedfhzgyls5r7yfxdesreverxsixgalfx5r7yfotwkguzx6rk'
]

# Visual inspection shows that 'xdesreverxsixgalfx' is a common string in all these short server names, confirmation:
for server in server_list:
    if 'xdesreverxsixgalfx' not in server:
        print('xdesreverxsixgalfx', 'not found in', server)

# Split by 'x' which seems to be the separator and reverse:
for word in 'xdesreverxsixgalfx'.split('x'):
    print(word[::-1])

# reversed
# is
# flag

