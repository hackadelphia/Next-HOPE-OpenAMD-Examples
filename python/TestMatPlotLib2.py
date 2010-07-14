import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
from matplotlib.patches import PathPatch

#here as a static string.
from  FakeFloorData import floor_data
from Floor import TestFloor

def map_of_floor(targetFloor = 1):
	floor = TestFloor(floor_data)
	floorBoundaries = floor.bounds()
	roomsOnFloor = floor.get_room_bounds_by_floor(targetFloor)
	

def draw_paths(targetFloor = 1):
	""" Make a compund path -- in this case two simple polygons, a rectangle
	and a triangle.  Use CLOSEOPOLY and MOVETO for the different parts of
	the compound path """
	vertices = []
	codes = []
	
	floor = TestFloor(floor_data)
	print floor_data
	floorBoundaries = floor.bounds()
	roomsOnFloor = floor.get_room_bounds_by_floor(targetFloor)
		
#	roomBounds = roomsOnFloor[0]
	for roomBounds in roomsOnFloor:
		print "new room"
		if(len(roomBounds) == 0):
			continue
		verts = roomBounds
		codes += [Path.MOVETO]
		vertices.append(verts.pop())
		while(len(verts)>0):
			codes += [Path.LINETO]
			vertices.append(verts.pop())
			
		codes += [Path.CLOSEPOLY]
		vertices.append([0,0])
		

#	codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
#	vertices = [(1,1), (1,2), (2, 2), (2, 1), (0,0)]
	
#	codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
#	vertices += [(4,4), (5,5), (5, 4), (0,0)]


	vertices = np.array(vertices, float)
	path = Path(vertices, codes)
	
	pathpatch = PathPatch(path, facecolor='None', edgecolor='green')
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.add_patch(pathpatch)
	ax.set_title('A compound path')
	
	ax.dataLim.update_from_data_xy(vertices)
	ax.autoscale_view()
	plt.show()



def histogram_of_room_sizes(targetFloor = 1):
	""" prints the room sizes as a histogram. Crazy, no?"""
	floor = TestFloor(floor_data)
	floorBoundaries = floor.bounds()

	area_per_room  = []
	roomsOnFloor = floor.get_room_bounds_by_floor(targetFloor)
	for vertices in roomsOnFloor:
		area_per_room.append(floor.area_by_verticies(vertices))
	area_per_room = [abs(x) for x in area_per_room]
#	help(plt.hist)
	print area_per_room
	n, bins, patches = plt.hist(area_per_room)


	plt.xlabel('Room Sizes')
	plt.ylabel('Number of Rooms')
	plt.title('Room sizes on ' +str(targetFloor) +" in m**2")
	plt.text(60, .025, r'some happy text and info')
	plt.grid(True)
	plt.show()

if __name__ == '__main__':
	#histogram_of_room_sizes()
	draw_paths()
