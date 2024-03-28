"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP100.htm
"""

# Find the eight-character Unicode code point for a hamburger, covered by a green box in the image below.

import unicodedata
hamburger = unicodedata.lookup('hamburger')

print(f"""
    glyph: {hamburger}
    codepoint: Dec: {ord(hamburger)}
    codepoint: Hex:  {hex(ord(hamburger))}
""")

# The answer is 0001f354
