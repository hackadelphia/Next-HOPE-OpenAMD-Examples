import json
import re
import urllib2

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
""" This file is a quick example of how to use the OpenAMD API, and what you can do with it.
This is by no means a complete implementation, but it is a good place to start, test
and tinker as you get ready to build your awesomely awesome app or project of your own. 

Educational comments are started as "#> 
Workflow comments  are written as # --
#TOOD: #TRICKY:  #BUG: and other such comments are self-explanitory

"""

#> This is our base URI for The Next HOPE instance of an OpenAMD server
g_openAMD_URI = "https://api.hope.net/"

#> This is a dictionary of 'data slices' as well as the section of the 
#> location on the data server where the data resides. Z.b. info on 'talks'
#> data is at "http://api.hope.net/api/talks"
g_slices = { 
			'location' : 'api/location',
			 'speakers' : 'api/speakers',
			 'talks' : 'api/talks',
			 'interests' : 'api/interests',
			 'users': '/api/users',
			 'stats': '/api/stats',
			 }

def slices():
	""" Returns the list of valid slices for this install of OpenAMD."""
	return g_slices.keys()

def uri_for_slice(sliceName):
	""" simple funciton to return a complete URI for a data slice. """
	return g_openAMD_URI + g_slices[sliceName]

def JSON_string_at_uri(uri):
	""" simple function to return the JSON string at a requested URI. """
	data = urllib2.urlopen(uri).read()
	return data	
	
def dictFromJSON(stringOfJSON):
	""" Returns a python dict created from the passed JSON string. """
	return json.loads(stringOfJSON, parse_float=True, parse_int=True, encoding='UTF-8')

def lazy_and_bad_way_to_get_dict():
	""" This is a lazy and bad way to get data in whole-slice increments. This
	is an example of something that works, but is a slow and poor way to run."""
	# -- fetch the uri for the whole talks slice
	uri = uri_for_slice('location')
	# -- fetch the JSON string for the whole slice
	data = JSON_string_at_uri(uri)		
	# -- turn that JSON string into a python list
	objs = dictFromJSON(data)

	return objs

class HopeAmdRewriterHandler(BaseHTTPRequestHandler):
	
	lastScaledMaxX = 80.0
	lastScaledMaxY = 80.0
	
	def do_GET(self):
		try:
			self.send_response(200)
			self.send_header('Content-type','text/plain')
			self.end_headers()
			x = self.amd_data_for_leica()
			print x
			self.wfile.write(x)
			return
		except IOError:
			self.send_error(404,'Someone Screwed Up')
		return

	def amd_data_scale_to_lica(self, rawLoc, cardinal = 'x'):
		if(cardinal == 'x'):
			print self.lastScaledMaxX
			tmp = float(rawLoc) - (self.lastScaledMaxX/2)
			tmp = tmp/(self.lastScaledMaxX/2)
			return tmp
		if(cardinal == 'y'):
			print self.lastScaledMaxY
			tmp = float(rawLoc) - (self.lastScaledMaxY/2)
			tmp = tmp/(self.lastScaledMaxY/2)
			return tmp
		return 0

	def data_list_from_loc(self, locData):
		z = '1'
		flag = '0'
		scaledX = self.amd_data_scale_to_lica(locData['x'])
		scaledY = self.amd_data_scale_to_lica(locData['y']) 		
		return map(str, ['',locData['user'],scaledX,scaledY,z,flag])
		
	def amd_data_for_leica(self):
		""" """
		retString = []
		locationDict = [{'user':'user2','x':'-20', 'y':'40'},{'user':'user1','x':'50', 'y':'60'} ]#lazy_and_bad_way_to_get_dict()
		# -- for each object in the list, grab it as  a dict, and look for 
		# -- having a track name, and that name being 'tesla'
		print locationDict
		for loc in locationDict:
			if u'x' in loc.keys():
				userData = self.data_list_from_loc(loc)
				retString.append('|'.join(userData))

		return '\n'.join(retString)
		
def main():
	try:
		server = HTTPServer(('',8081),HopeAmdRewriterHandler)
		print 'server started'
		server.serve_forever()
	except KeyboardInterrupt:
		print "^C received, killing server"
		server.socket.close()


#> This is a pretty standard main statement for Python, and if you run 
#> "python $THIS_FILE_NAME this will run. This just grabs/shows the locations data
if __name__ == '__main__':

	main()	

	