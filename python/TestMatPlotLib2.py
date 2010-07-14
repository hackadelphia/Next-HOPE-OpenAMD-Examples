import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#here as a static string.
from  FakeFloorData import floor_data
from Floor import TestFloor

def printThing():

	fig = plt.figure()
	ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])
	
	#im = ax.imshow(np.random.rand(10,10))
	
	p = patches.Rectangle([10,10], 10,10, facecolor="orange", edgecolor="red")
	
	plt.gca().add_patch(p)
	
	plt.draw()
	plt.show()
	
	
	#im.set_clip_path(patch)
	
	
	#matplotlib.rcParams['axes.unicode_minus'] = False
	#ax = fig.add_subplot(111)
	#ax.plot(floor.allVerticesX(), floor.allVerticesY(), 'o')
	#ax.set_title('Using hypen instead of unicode minus')
	#plt.show()


def histogram_of_room_sizes(targetFloor = 1):
	""" prints the room sizes as a histogram. Crazy, no?"""
	floor = TestFloor(floor_data)
	floorBoundaries = floor.bounds()

	area_per_room  = []
	roomsOn18 = floor.get_room_bounds_by_floor(targetFloor)
	for vertices in roomsOn18:
		area_per_room.append(floor.area_by_verticies(vertices))
	area_per_room = [abs(x) for x in area_per_room]
#	help(plt.hist)
	print area_per_room
	n, bins, patches = plt.hist(area_per_room)


	plt.xlabel('Room Sizes')
	plt.ylabel('Number of Rooms')
	plt.title('Room sizes on ' +str(targetFloor) +" in m**2")
	plt.text(60, .025, r'some happy text and info')
#	plt.axis([40, 160, 0, 0.03])
	plt.grid(True)
	plt.show()

if __name__ == '__main__':
	histogram_of_room_sizes()