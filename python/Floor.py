import logging

class TestRoom():
	
	dict = None
	name = None
	vertices = None
	floor = None
	access = None
	def __init__(self,roomDict):
		self.dict = roomDict
		self.name = self.dict['name']
		self.vertices = self.dict['vertices'] 
		self.floor = self.dict['floor']
		self.access = self.dict['access']

#	def size():
#		"returns a tuple of the room's size"

#	def startPoints():
#		"returns a 'upper left' most point of a room"
		
class TestFloor():
	
	rawFloorDict = {} #raw data dictionary from floor data
	floorDict = {} #list of rooms
	
	
	def __init__(self, floorDict):
		self.rawFloorDict = floorDict
		for entry in self.rawFloorDict:
			if entry['floor'] not in self.floorDict.keys():
				logging.info("adding a floor")
				self.floorDict[entry['floor']] = []
			else:
				logging.info("making rooms")
				self.floorDict[entry['floor']].append(TestRoom(entry))

	def area_by_verticies(self, vertices):
		if len(vertices) == 0:
			return 0.0
		elif len(vertices) == 4:
			size = (vertices[2][1] -  vertices[0][1]) * ( vertices[2][0] -  vertices[0][0])
			return size
		else:
			logging.error("area_by_verticies can't handle more than 2 verticies")
			return 0
			
			
	def get_room_bounds_by_floor(self, floorNumber = None):
		"""Returns the bounding verticies for each room on a floor."""
		x = []
		if floorNumber == None:
			for area in self.rawFloorDict:
				if 'vertices' in area:
					x.append(area['vertices'])
		elif floorNumber in self.floorDict.keys():
			logging.error('maiking verticies')
			for roomObj in self.floorDict[floorNumber]:
				x.append(roomObj.vertices)				
		return x
		
	def allVertices(self, floorNumber=None):
		x = []
		#logging.error("all verticies is not correct")
		if floorNumber == None:
			for area in self.rawFloorDict:
				if 'vertices' in area:
					x.extend(area['vertices'])
		elif floorNumber in self.floorDict.keys():
			#logging.error('maiking verticies')
			for roomObj in self.rawFloorDict[floorNumber]:
				x.extend(roomObj.vertices)				
		return x
		pass
				
	def allVerticesX(self):
		return [ x for x,y in self.allVertices()]

	def allVerticesY(self):
		return [ y for x,y in self.allVertices()]
	
	def bounds(self):
		minX = min(self.allVerticesX())
		minY = min(self.allVerticesY())
		maxX = max(self.allVerticesX())
		maxY = max(self.allVerticesY())
		bounds = ((minX,minY),(maxX,minY),(maxX,maxY),(minX,maxY))
		logging.info("Bounds are" + str(bounds))
		return bounds
	
	