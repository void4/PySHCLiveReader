from time import sleep

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from memory import MemoryReader
from maps import *

reader = MemoryReader("Crusader.exe", {"PlayerTable":V1_2})

def liveplot():
	fig = plt.figure()

	AXES = "Gold Units Popularity".split()

	axes = [[fig.add_subplot(1,3,ax+1), [], [[] for i in range(8)]] for ax in range(len(AXES))]

	def animate(i):

		tables = reader.runOnce()

		for axi, ax in enumerate(axes):

			# Limit x and y lists to 20 items
			#ax[1] = ax[1][-20:]
			#ax[2] = [a[-20:] for a in ax[2]]

			ax[0].clear()

			ax[1].append(i)

			for playerindex in range(8):
				player = tables["PlayerTable"][playerindex]
				meta = [m for m in player if m.name==AXES[axi]][0]
				ax[2][playerindex].append(meta.value)
				ax[0].plot(ax[1], ax[2][playerindex], label=f"Player{playerindex} - {meta.value}")

			#print(ax[0], dir(ax[0]))
			#ax[0].ylabel(AXES[axi])
			ax[0].legend()

		# Format plot
		#plt.xticks(rotation=45, ha='right')
		#plt.subplots_adjust(bottom=0.30)
		plt.title("Game stats")
		#plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials
		#plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo

	# Set up plot to call animate() function periodically
	ani = animation.FuncAnimation(fig, animate, interval=100)
	plt.show()


"""
while True:
	tables = reader.runOnce()
	print(tables)
	sleep(1)
"""
if __name__ == "__main__":
	liveplot()
