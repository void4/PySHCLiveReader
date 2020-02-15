from sys import argv
from pymem import Pymem
from copy import deepcopy

pm = Pymem("Crusader.exe")#"Stronghold_Crusader_Extreme.exe")

start = 0x011F2938
step = 2

history = []

def converge(target):
    #print(history)
    if isinstance(target, int):
        searchfuncs = [pm.read_int, pm.read_short]
    elif isinstance(target, str):
        searchfuncs = [pm.read_string]
    else:
        raise TypeError("Unsupported target type", type(target), target)
    history.append({})
    for i in range(5000000):
        try:
            address = start + i*step
            if len(history) == 1 or address in history[-2]:
                values = [f(address) for f in searchfuncs]
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
        try:
            s = pm.read_string(addr)
        except UnicodeDecodeError:
            s = "???"
        print(hex(addr), pm.read_int(addr), pm.read_short(addr), s)
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
