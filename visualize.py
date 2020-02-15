from time import sleep

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

def liveplot(reader, vizax):
	fig = plt.figure()

	fig_size = plt.gcf().get_size_inches() #Get current size
	sizefactor = 1.8 #Set a zoom factor
	# Modify the current size by the factor
	plt.gcf().set_size_inches(sizefactor * fig_size)

	axes = [[fig.add_subplot(3,1,ax+1), [], [[] for i in range(8)]] for ax in range(len(vizax))]

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
				meta = [m for m in player if m.name==vizax[axi]][0]
				ax[2][playerindex].append(meta.value)
				ax[0].plot(ax[1], ax[2][playerindex], label=f"Player{playerindex} - {meta.value}")

			#print(ax[0], dir(ax[0]))
			ax[0].set_ylabel(vizax[axi])
			ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))

		# Format plot
		#plt.xticks(rotation=45, ha='right')
		#plt.subplots_adjust(bottom=0.30)
		#plt.title("Game stats")
		plt.subplots_adjust(right=0.7)
		#plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials
		#plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo

	# Set up plot to call animate() function periodically
	ani = animation.FuncAnimation(fig, animate, interval=100)
	plt.show()
