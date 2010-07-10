import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms
import matplotlib.text as mtext

#HACK: since floor data is NOT AVAILABLE, I'm creating floor data 
#here as a static string.
from  FakeFloorData import floor_data

hacky_scale_factor = 20.0


class TestFloor():
	
	floorDict = {}
	
	def __init__(self, floorDict):
		self.floorDict = floorDict

	def allVertices(self):
		x = [] 
		for area in self.floorDict:
			if 'vertices' in area:
				x.extend(area['vertices'])
		return x
		
	def allVerticesX(self):
		self.allVertices()
		return [ x for x,y in self.allVertices()]
	def allVerticesY(self):
		return [ y for x,y in self.allVertices()]
	
	def verticies(self):
		minX = min(self.allVerticesX())
		minY = min(self.allVerticesY())
		maxX = max(self.allVerticesX())
		maxY = max(self.allVerticesY())
		return ((minX,minY),(maxX,minY),(maxX,maxY),(minX,maxY))

class TestRoom(lines.Line2D):

   def __init__(self, amdRoomDict, *args, **kwargs):
      # we'll update the position when the line data is set
#      x, y = np.random.rand(2, 20)
      x, y = self.room_outline(floor_data[0])
      self.text = mtext.Text(0, 0, '')
      lines.Line2D.__init__(self, x,y, *args, **kwargs)

      # we can't access the label attr until *after* the line is
      # inited
      self.text.set_text(self.get_label())

   def room_outline(self, dict):
		x,y = [],[]
		if 'vertices' in dict:
			for v in dict['vertices']:
				x.append(v[0]/hacky_scale_factor) 
				y.append(v[1]/hacky_scale_factor)
		else:
			pass
		return x,y

   def set_figure(self, figure):
      self.text.set_figure(figure)
      lines.Line2D.set_figure(self, figure)

   def set_axes(self, axes):
      self.text.set_axes(axes)
      lines.Line2D.set_axes(self, axes)

   def set_transform(self, transform):
      # 2 pixel offset
      texttrans = transform + mtransforms.Affine2D().translate(2, 2)
      self.text.set_transform(texttrans)
      lines.Line2D.set_transform(self, transform)


   def set_data(self, x, y):
      if len(x):
         self.text.set_position((x[-1], y[-1]))

      lines.Line2D.set_data(self, x, y)

   def draw(self, renderer):
      # draw my label at the end of the line with 2 pixel offset
      lines.Line2D.draw(self, renderer)
      self.text.draw(renderer)




"""
fig = plt.figure()
ax = fig.add_subplot(111)
line = TestRoom(floor_data, mfc='red', ms=12, label='line label')
#line.text.set_text('line label')
line.text.set_color('red')
line.text.set_fontsize(16)


ax.add_line(line)


#plt.show()
"""
f = TestFloor(floor_data)
print f.verticies()