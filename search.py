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
    target = int(argv[1])
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
