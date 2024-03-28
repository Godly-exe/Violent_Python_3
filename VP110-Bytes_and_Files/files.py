"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP110.htm
"""

# Create a file named infile containing the string 'HELLO'
text_file = open('infile', 'w')
n = text_file.write('HELLO')
text_file.close()

# Read the file one byte at a time
print("Reading 'infile'")
with open('infile', 'rb') as f:
    byte = f.read(1)
    while byte != b"":
        print(byte)
        byte = f.read(1)

# Copy infile to outfile
print("Reading 'infile' and writing 'outfile'")
with open("infile", "rb") as f:
    with open("outfile", "wb") as g:
        byte = f.read(1)
        while byte != b"":
            print(byte)
            g.write(byte)
            byte = f.read(1)


