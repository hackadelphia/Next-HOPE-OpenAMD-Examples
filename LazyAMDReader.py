import json
import re
import urllib2
""" This file is a quick example of how to use the OpenAMD API, and what you can do with it.
This is by no means a complete implementation, but it is a good place to start, test
and tinker as you get ready to build your awesomely awesome app or project of your own. 

#> Are Educational comments
# -- Are workflow comments 
#TOOD: #TRICKY:  #BUG: and other such comments are self-explanitory

"""


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


#new tech, activism, radio, lockpicking, crypto, privacy, ethics, telephones, social engineering, hacker spaces, hardware hacking, nostalgia, communities, science, government, network security, malicious software, pen testing, web, niche hacks, media


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


def JSON_for_entire_slice(sliceName):
	""" simple function to return the JSON string for an entire JSON slice.
	Don't be a jerk and use this often, it eats bandwith. use more specific 
	fetch tools that are below."""
	sliceUri = uri_for_slice(sliceName)
	return JSON_string_at_uri(sliceUri)

	
def dictFromJSON(stringOfJSON):
	""" Returns a python dict created from the passed JSON string. """
	return json.loads(stringOfJSON, parse_float=True, parse_int=True, encoding='UTF-8')


def JSONFromDict(dict):
	""" returns a pretty printed JSON string from a python object. """
	return json.dumps(dict, sort_keys=True, indent=4)
	
def JSONFromDict(slice, limitDict):
	"""function tries to fetch data from slice, iff the key pairs in 'limitDict' 
	are matched. If there is no limitDict, or it is empty, the whole slice is."""
	if(limitDict == None or len(limitDict.keys()) == 0):
		return JSON_for_entire_slice(slice)
	else:
		base = JSON_for_entire_slice(slice)
		# -- limits are the form of '?x=y&z=k' 
		limits = '?'
		for x in d.keys():
			limits += str(x)+'='+str(d[x])+'&'
		limits.rstrip('&')
		

def filter_for_slice_uri(slice, filterDict):
	"""Returns a valid query string paramaeters list from a slice,
	and a list of query and value pairs. """
	uri = uri_for_slice('talks')
	#> This magic takes a dict, and turns it into a query string
	query_string =  '&'.join(
		[k+'='+urllib2.quote(str(v)) for (k,v) in filterDict.items()])

	#TODO: test other filters, esp. list's passed in the filter dict

	#> using 'x'.join is a faster and sleeker string builder than the + operator in python
	return '?'.join( (uri,query_string) )
	
def sleekAndSmartWayToGetData():
	"""This is an example of a fast and smart way to grab data from the API."""
	# -- fetch the uri for the data in a slice that matches filters.
	slice = 'talks'
	filterDict = {'track':'Tesla'}
	uri =  filter_for_slice_uri(slice, filterDict)
	print uri
	# -- fetch the JSON string for the whole slice
	data = JSON_string_at_uri(uri)		
	# -- turn that JSON string into a python list
	obj = dictFromJSON(data)
	# -- for each object in the list, grab it as  a dict, and look for 
	# -- having a track name, and that name being 'tesla'
	for talk in obj:
		print talk 

def lazyAndBayWayToGetData():
	""" This is a lazy and bad way to get data in whole-slice increments. This
	is an example of something that works, but is a slow and poor way to run."""
	# -- fetch the uri for the whole talks slice
	uri = uri_for_slice('talks')
	# -- fetch the JSON string for the whole slice
	data = JSON_string_at_uri(uri)		
	# -- turn that JSON string into a python list
	obj = dictFromJSON(data)

	# -- for each object in the list, grab it as  a dict, and look for 
	# -- having a track name, and that name being 'tesla'
	for talk in obj:
		if u'track' in talk.keys() and talk[u'track'] == u"Tesla":
			print talk
		else: print 'nomatch'



#> This is a pretty standard main statement for Python, and if you run 
#> "python $THIS_FILE_NAME this will run. This just grabs/shows the locations data


if __name__ == '__main__':
#	lazyAndBadWayToGetData()
	sleekAndSmartWayToGetData()	