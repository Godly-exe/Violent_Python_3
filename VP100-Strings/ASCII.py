"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

a = '\x41\x42\xff'
print(a)
print(a[0])
print(a[1])
print(a[2])

# There are 4 bytes in the encoded object, not three, and none of them are ff
b = a.encode()
print(hex(b[0]))
print(hex(b[1]))
print(hex(b[2]))
print(hex(b[3]))

# Python3 uses Unicode UTF-8 encoding by default instead of ASCII.
# the character '\xff' in the string is interpreted a Unicode Code Point, and it's stored in two bytes
# UTF-8 characters have variable length, from one to four bytes.

print('\x41')  # A
print('\U41')  # (unicode error) 'unicodeescape' codec can't decode bytes in position 0-3: truncated \UXXXXXXXX escape
print('\U0041')  # (unicode error) 'unicodeescape' codec can't decode bytes in position 0-5: truncated \UXXXXXXXX escape
print('\U000041')  # (unicode error) 'unicodeescape' codec can't decode bytes in position 0-7: truncated \UXXXXXXXX escape
print('\U00000041')  # A
print('\x41'.encode())  # b'A'
print('\U00000041'.encode())  # b'A'
print('\x41'.encode().hex())  # 41
print('\U00000041'.encode().hex())  # 41

print('\xff')  # ÿ
print('\Uff')  # (unicode error) 'unicodeescape' codec can't decode bytes in position 0-3: truncated \UXXXXXXXX escape
print('\U00ff')  # (unicode error) 'unicodeescape' codec can't decode bytes in position 0-5: truncated \UXXXXXXXX escape
print('\U0000ff')  # (unicode error) 'unicodeescape' codec can't decode bytes in position 0-7: truncated \UXXXXXXXX escape
print('\U000000ff')   # ÿ
print('\xff'.encode())  # b'\xc3\xbf'
print('\U000000ff'.encode())  # b'\xc3\xbf'

