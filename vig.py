#!/opt/anaconda3/bin/python
import sys
import math
import random

Z26star = [a for a in range(26) if math.gcd(a,26)==1]
Z26 = range(0,26)

vigKeys = open("vigKeys.txt","r").readlines()
vigKeys = [v[:-1] for v in vigKeys]


key = random.choice(vigKeys)
print("key is {}".format(bytes(key.encode())),file=sys.stderr)

def encrypt(key):
    out= ""
    i=0
    L=len(key)
    for line in sys.stdin:
        for p in line:
            if p not in [chr(v) for v in range(65,65+26)]:
                continue
            n_p = ord(p)-65
            n_k = ord(key[i%L])-65
            i += 1
            n_c = (n_p + n_k)%26
            c = chr(n_c+65)
            out += c
    print(out)

def decrypt(key):
    out= ""
    i=0
    L=len(key)
    for line in sys.stdin:
        for c in line:
            if c not in [chr(v) for v in range(65,65+26)]:
                continue
            n_c = ord(c)-65
            n_k = ord(key[i%L])-65
            i += 1
            n_p = (n_c - n_k)%26
            p = chr(n_p+65)
            out += p
    print(out)

assert(len(sys.argv)==2)

assert(sys.argv[1] in ['e','d'])

if sys.argv[1]=='e':
    encrypt(key)
else:
    decrypt(key)




