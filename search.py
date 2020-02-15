from sys import argv
from pymem import Pymem
from copy import deepcopy

pm = Pymem("Stronghold_Crusader_Extreme.exe")



start = 0x011F2938
step = 4
#V1.2.1-E
#0x122c760 P1 Gold
history = []

def converge(target):
    #print(history)
    history.append({})
    for i in range(100000):
        try:
            address = start + i*step
            value = pm.read_int(address)
            if value == target:
                #print("FOUND")
                if len(history) == 1 or address in history[-2]:
                    print(hex(address), value)
                    history[-1][address] = value
        except UnicodeDecodeError:
            pass

if len(argv) > 1:
    arg1 = argv[1]
    if arg1 == "read":
        addr = int(argv[2], 16)
        print(pm.read_int(addr))
        exit(0)
    try:
        target = int(arg1)
    except ValueError:
        exit(1)
    converge(target)

while True:
    try:
        inp = input(">")
        if inp == "q":
            break
        target = int(inp)
    except ValueError:
        continue
    converge(target)
