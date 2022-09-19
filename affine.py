#!/opt/anaconda3/bin/python
import sys
import math
import random

Z26star = [a for a in range(26) if math.gcd(a,26)==1]
Z26 = range(0,26)

a,b = random.choice(Z26star),random.choice(Z26)
a,b = 11,17
print("WARNING KEY IS HARDCODED")

def encrypt():
    out= ""
    for line in sys.stdin:
        for p in line:
            if p not in [chr(v) for v in range(65,65+26)]:
                continue
            n_p = ord(p)-65
            n_c = (a*n_p + b)%26
            c = chr(n_c+65)
            out += c
    print(out)
def decrypt():
    out=""
    for line in sys.stdin:
        for c in line:
            if c not in [chr(v) for v in range(65,65+26)]:
                continue
            n_c = ord(c)-65
            n_p = (invert(a)*(n_c - b))%26
            p = chr(n_p+65)
            out += p
    print(out)

def invert(_a):

    b = [x for x in range(26) if (x*_a)%26==1]
    assert(len(b)==1)
    #print("{} inverse is {}".format(_a,b[0]))
    return b[0]

assert(len(sys.argv)==2)

assert(sys.argv[1] in ['e','d'])
if sys.argv[1]=='e':
    encrypt()
else:
    decrypt()




