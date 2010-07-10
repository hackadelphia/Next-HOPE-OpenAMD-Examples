import json
import re
import urllib2

#> This is our base URI for The Next HOPE instance of an OpenAMD server
g_openAMD_URI = "http://api.hope.net/"

#> This is a dictionary of 'data slices' as well as the section of the 
#> location on the data server where the data resides. Z.b. info on 'talks'
#> data is at "http://api.hope.net/api/talks"
g_slices = { 
			'locations' : 'api/locations',
			 'speakers' : 'api/speakers',
			 'talks' : 'api/talks',
				 'interests' : 'api/interests',
			 'users': '/api/users',
			 'stats': '/api/stats',
			 }

#> These are lists of fields in each slice.
g_slice_fields = {
			'locations' : ('area','time','x','y','user','button'), 
			 'speakers' : ('name','bio'), 
			 'talks' :  ('speakers','title','abstract','time','track','interests'), 
			 'interests' : (), #this is a free-from set of tags
			 'users': ('name','x','y','interests'),
			 'stats': ('poptalks','age'), #TRICKY:TODO: examples, there are not set yet
}

def JSON_string_at_uri(uri):
	""" simple function to return the JSON string at a requested URI. """
	data = urllib2.urlopen(uri).read()
	return data	

	
def dictFromJSON(stringOfJSON):
	""" Returns a python dict created from the passed JSON string. """
	return json.loads(stringOfJSON, parse_float=True, parse_int=True, encoding='UTF-8')

	
class HopeAPI:

	def uri_for_slice(self, sliceName):
		""" simple funciton to return a complete URI for a data slice. """
		return g_openAMD_URI + g_slices[sliceName]
		
	def filter_for_slice_uri(self, slice):
		"""Returns a valid query string paramaeters list from a slice,
		and a list of query and value pairs. """
		uri = self.uri_for_slice(slice)
		#> This magic takes a dict, and turns it into a query string
		query_string =  '&'.join(
			[k+'='+urllib2.quote(str(v)) for (k,v) in self.filterDict.items()])
	
		#TODO: test other filters, esp. list's passed in the filter dict
	
		#> using 'x'.join is a faster and sleeker string builder than the + operator in python
		return '?'.join( (uri,query_string) )
	
	def __init__(self, filter = None):
		self.filterDict = filter
		
	def __getattr__(self, slice):
		"""This is an example of a fast and smart way to grab data from the API."""
		if not g_slices.has_key(slice):
			raise Exception('Unsupported slice name: ' + slice)
			
		if self.filterDict == None:
			# -- fetch the uri for the whole talks slice
			uri = self.uri_for_slice(slice)
		else:		
			# -- fetch the uri for the data in a slice that matches filters.
			uri =  self.filter_for_slice_uri(slice)
		# -- fetch the JSON string for the whole slice
		data = JSON_string_at_uri(uri)		
		# -- turn that JSON string into a python list
		return dictFromJSON(data)
