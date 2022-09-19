#! /opt/anaconda3/bin/python

ct = open("my_caesar_ct.txt").read()

for key in range(0,26):
    print("Trying key {}".format(chr(key+65)))
    out = ""
    for c in ct[1000:2000]:
        out += chr((ord(c)-65 - key)%26+65)
    print(out)
    print("\n*****")


