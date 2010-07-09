import unittest

import LazyAMDReader

class TestTrivialReader(unittest.TestCase): 
	"""This class is a very simple Unit Test for testing the data Reader.
	This isn't a best designed class, it is to be an example for beginners to understand
	tests, and to check if/when we change data URI's"""
	
	def test_slices_resolve_to_uri(self):
		""" This test fectches the list of data slices, and tries to fetch
		 the base url for fecting data from that slice.  Fails if any slice
		 fails to return a URI. """
		slices = LazyAMDReader.slices()
		for s in slices:
			uri = LazyAMDReader.uri_for_slice(s)
			self.assertNotEqual(uri, None)
	
	def test_slices_can_return_data(self):
		""" This test fectches the list of data slices, and tries to fetch
		the full data set from that dataslice by requesting the 'root' url
		for that slice (to return all data. Fails if any 'root slice' request
		returns a None string"""
		slices = LazyAMDReader.slices()
		for s in slices:
			uri = LazyAMDReader.uri_for_slice(s)
			json = LazyAMDReader.JSON_string_at_uri(uri)
			self.assertNotEqual(json, None)


if __name__ == '__main__':
	unittest.main() #unittest.main

