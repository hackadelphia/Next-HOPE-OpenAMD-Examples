import json
import re
import urllib2


g_openAMD_URI = "http://api.hope.net/"
g_slices = {'locations' : 'api/locations',
			 'speakers' : 'api/speakers',
			 'talks' : 'api/talks',
			 'interests' : 'api/interests',
			 }

def dictFromJSON(stringOfJSON):
	""" Returns a python dict created from the passed JSON string"""
	return json.loads(stringOfJSON, parse_float=True, parse_int=True, encoding='UTF-8')

def JSONFromDict(dict):
	""" returns a pretty printed JSON string from a python object. """
	return json.dumps(dict, sort_keys=True, indent=4)

def uri_for_slice(sliceName):
	return g_openAMD_URI + g_slices[sliceName]

def slices():
	return g_slices.keys()

def JSON_string_at_uri(uri):
	data = urllib2.urlopen(uri).read()
	return data	

if __name__ == '__main__':
	uri = uri_for_slice('locations')
	data = JSON_string_at_uri(uri)	
	obj = dictFromJSON(data)

	d2 = JSONFromDict(obj)
	print d2