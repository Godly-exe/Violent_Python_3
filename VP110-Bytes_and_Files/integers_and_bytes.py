"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP110.htm
"""

# Integers
i = 1
print(i, type(i))
j = i + 1
print(j, type(j))

# Bytes
a = b'\x01'
print(a, type(a))
# b = a + 1  # TypeError: can't concat int to bytes

# Convert byte to integer
b = a[0]
print(b, type(b))
c = b + 1
print(c, type(c))

# Convert byte to integer, add the integers, convert back to byte
a = b'\x01'
print(a, type(a))
b = a[0]
print(b, type(b))
c = b + 1
print(c, type(c))
d = bytes([c])
print(d, type(d))


