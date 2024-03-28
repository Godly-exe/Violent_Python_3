"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

# Find the eight-character Unicode code point for a capital Sigma, covered by a green box in the image below.

"""
for x in range(0, 0xfff+1):
    if chr(x).isprintable():
        print(f"x is {x}, chr(x) is {chr(x)}")
"""

look_for = 'Σ'
for x in range(0, 0xfff+1):
    if chr(x) == look_for:
        print(f"x is {x} ({hex(x)}), which is the unicode for {look_for}")

# x is 931 (0x3a3), which is the unicode for Σ
# Answer is 000003a3

