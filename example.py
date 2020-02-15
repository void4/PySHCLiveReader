# If you want to create your own visualizations, bots etc. using the live data
# Use it like this:
from memory import MemoryReader
from tables import *

reader = MemoryReader("Crusader.exe", {"PlayerTable": V1_2})

while True:
	tables = reader.runOnce()
    # tables now contains the most recent values of all tracked addresses
	print(tables)
	sleep(1)
