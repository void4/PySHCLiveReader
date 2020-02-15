# If you want to create your own visualizations, bots etc. using the live data
# Use it like this:
from memory import MemoryReader
from maps import *

#"Stronghold_Crusader_Extreme.exe"
reader = MemoryReader("Crusader.exe", {"PlayerTable": V1_2})

while True:
	tables = reader.runOnce()
	print(tables)
	sleep(1)
