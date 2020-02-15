from memory import MemoryReader

#V1.2.1-E
V1_2_1_E = """Name:32:s Gold:4 Units:4 Popularity:4 Population:2 Housing:2
- 0x122c760
- 0x1230154 0x1230000
- 0x1233b48 0x1242348
- 0x123753c 0x12373e8
- 0x123af30 0x123addc
- 0x123e924
- 0x1242318
- 0x1245d0c"""

V1_41E_UCP2_13 = """Name:32:s Gold:4 Units:4 Popularity:4 Population:2 Housing:2
0x024BA286 0x011F2938 0x011F27E4 0x011F2870 0x011F45AC 0x011F24A0
0x024BA2E0 0x011F632C 0x011F61D8 0x011F6264 0x011F7FA0 0x011F5E94
0x024BA33A 0x011F9D20 0x011F9BCC 0x011F9C58 0x011FB994 0x011F9888
0x024BA394 0x011FD714 0x011FD5C0 0x011FD64C 0x011FF388 0x011FD27C
0x024BA3EE 0x01201108 0x01200fb4 0x01201040 0x01202D7C 0x01200C70
0x024BA448 0x01204AFC 0x012049A8 0x01204A34 0x01206770 0x01204664
0x024BA4A2 0x012084F0 0x0120839C 0x01208428 0x0120A164 0x01208058
0x024BA4FC 0x0120BEE4 0x0120BD90 0x0120BE1C 0x0120DB58 0x120BA4C
"""


LeaderBoard = """Name:32:s, TotalGold:4 TroopsProduced:4 FoodProduced:4 StoneProduced:4 IronProduced:4 WoodProduced:4 BuildingsLost:4 BuildingsDestroyed:4 HighestPopulation:4 Housing:2"""

reader = MemoryReader("Stronghold_Crusader_Extreme.exe", {"PlayerTable":V1_2_1_E})

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

def liveplot():
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	xs = []
	ys = [[] for i in range(8)]

	def animate(i):

		tables = reader.runOnce()

		# Limit x and y lists to 20 items
		#xs = xs[-20:]
		#ys = ys[-20:]

		# Add x and y to lists
		xs.append(i)
		ax.clear()
		for playerindex in range(8):
			player = tables["PlayerTable"][playerindex]
			gold = [m for m in player if m.name=="Gold"][0]
			ys[playerindex].append(gold.value)
			ax.plot(xs, ys[playerindex], label=f"Player{playerindex} - {gold.value}")

		# Format plot
		plt.xticks(rotation=45, ha='right')
		plt.subplots_adjust(bottom=0.30)
		plt.title("Game stats")
		plt.ylabel('Gold')
		plt.legend()
		#plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials
		#plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo

	# Set up plot to call animate() function periodically
	ani = animation.FuncAnimation(fig, animate, interval=50)
	plt.show()

from time import sleep
"""
while True:
	tables = reader.runOnce()
	print(tables)
	sleep(1)
"""
if __name__ == "__main__":
	liveplot()
