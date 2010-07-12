import json
import re
import urllib2



class HopeAPI:

	#> These are lists of fields in each slice.
	slice_fields = {
			'locations' : ('area','time','x','y','user','button'), 
			 'speakers' : ('name','bio'), 
			 'talks' :  ('speakers','title','abstract','time','track','interests'), 
			 'interests' : (), #this is a free-from set of tags
			 'users': ('name','x','y','interests'),
			 'stats': ('poptalks','age'), #TRICKY:TODO: examples, there are not set yet
	}

	#> This is a dictionary of 'data slices' as well as the section of the 
	#> location on the data server where the data resides. Z.b. info on 'talks'
	#> data is at "http://api.hope.net/api/talks"
	slices = { 
			'locations' : 'api/locations',
			 'speakers' : 'api/speakers',
			 'talks' : 'api/talks',
				 'interests' : 'api/interests',
			 'users': '/api/users',
			 'stats': '/api/stats',
			 }
	#> This is our base URI for The Next HOPE instance of an OpenAMD server
	openAMD_URI = "http://api.hope.net/"




	def uri_for_slice(self, sliceName):
		""" simple funciton to return a complete URI for a data slice. """
		return self.openAMD_URI + self.slices[sliceName]
		
	def filter_for_slice_uri(self, slice, filterDict):
		"""Returns a valid query string paramaeters list from a slice,
		and a list of query and value pairs. """
		uri = self.uri_for_slice(slice)
		#> This magic takes a dict, and turns it into a query string
		query_string =  '&'.join(
			[k+'='+urllib2.quote(str(v)) for (k,v) in filterDict.items()])
	
		#TODO: test other filters, esp. list's passed in the filter dict
	
		#> using 'x'.join is a faster and sleeker string builder than the + operator in python
		return '?'.join( (uri,query_string) )
	
	def __init__(self, filter = None):
		pass
		
	@classmethod
	def JSON_string_at_uri(cls, uri):
		""" simple function to return the JSON string at a requested URI. """
		data = urllib2.urlopen(uri).read()
		return data	

	def json_from_slice(self, slice, filterDict):
		uri = self.uri_for_slice(slice)
		if(filterDict and filterDict != None):
			query_string = '&'.join(
				[k+'='+urllib2.quote(str(v)) for (k,v) in filterDict.items()])
			uri = '?'.join( (uri,query_string) )
	
		return self.JSON_string_at_uri(uri)
	
	def __getattr__(self, slice):			
		""" This function does magic to allow a user to call 
		appInstance.sliceName(filterDict) in order get JSON for a slice as 
		filtered for the intersection of all dictionary terms. 
		See dev notes in the code for more info
		"""
		# -- getattr is 'only called when no funciion or variable was matched'
		
		# -- if we do not have a slice of that name, exception
		if not self.slices.has_key(slice):
			raise Exception('Unsupported slice name: ' + slice)
			
		# -- otherwise return a function that takes 0 or 1 filterDict entries
		return lambda filterDict=None : self.json_from_slice(slice,filterDict)

if __name__ == '__main__':
	api = HopeAPI()
	print api.locations()
	
	print api.talks({'track': 'Tesla'})