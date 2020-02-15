from memory import MemoryReader
from visualize import liveplot
from tables import *

reader = MemoryReader("Crusader.exe", {"PlayerTable": V1_2})

if __name__ == "__main__":
	# First argument is the MemoryReader
	# Second argument is a list of columns that will be plotted
	liveplot(reader, "Gold Units Popularity".split())
