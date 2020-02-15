from sys import argv
from pymem import Pymem

pm = Pymem("Stronghold_Crusader_Extreme.exe")

target = int(argv[1])

start = 0x011F2938
step = 4
#0x122c760
for i in range(100000):
    try:
        address = start + i*step
        value = pm.read_int(address)
        if value == target:
            print("FOUND")
            print(hex(address), address, value)
    except UnicodeDecodeError:
        pass
