from sys import argv
from pymem import Pymem
from copy import deepcopy

pm = Pymem("Stronghold_Crusader_Extreme.exe")

start = 0x011F2938
step = 4

history = []

def converge(target):
    #print(history)
    history.append({})
    for i in range(25000000):
        try:
            address = start + i*step
            if len(history) == 1 or address in history[-2]:
                values = [pm.read_int(address), pm.read_short(address), pm.read_string(address)]
                if target in values:
                    #print("FOUND")
                    print(hex(address), values)
                    history[-1][address] = values
        except UnicodeDecodeError:
            pass

if len(argv) > 1:
    arg1 = argv[1]
    if arg1 == "read":
        addr = eval(argv[2])#int(argv[2], 16)
        print(hex(addr), pm.read_int(addr), pm.read_short(addr), pm.read_string(addr))
        exit(0)
    try:
        target = eval(arg1)
    except ValueError:
        exit(1)
    converge(target)

while True:
    try:
        #if inp=="d": import pdb; pdb.set_trace()
        inp = input(">")
        if inp == "q":
            break
        elif inp == "<":
            print("Going back <1")
            history = history[:-1]
        else:
            target = eval(inp)
            converge(target)
    except ValueError:
        continue
