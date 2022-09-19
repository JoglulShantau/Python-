fp = open("headas.txt")

rl = fp.readlines()

for entry in set(rl):
    print(entry)

