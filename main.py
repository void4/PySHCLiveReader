from memory import MemoryReader
from visualize import liveplot
from maps import *

#"Stronghold_Crusader_Extreme.exe"
reader = MemoryReader("Crusader.exe", {"PlayerTable":V1_2})

"""
while True:
	tables = reader.runOnce()
	print(tables)
	sleep(1)
"""
if __name__ == "__main__":
	liveplot(reader, "Gold Units Popularity".split())
