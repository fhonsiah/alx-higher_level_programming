#!/usr/bin/python3
alphabet = ""
for i in range(ord('z'), ord('a')-1, -1):
    alphabet = "{}{}".format(alphabet, chr(i) if i % 2 else chr(i-32))
print(alphabet[::-1])
