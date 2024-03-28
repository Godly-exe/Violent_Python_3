"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

greet = "Hello, World!"
print(greet)

print(f"First 3 characters of the string '{greet}':  ", greet[0:3])
print(f"Second 3 characters of the string '{greet}': ", greet[3:6])
print(f"Last 3 characters of the string '{greet}':   ", greet[-3:])
print("Portion before comma:                              ", greet[:(greet.find(","))])
