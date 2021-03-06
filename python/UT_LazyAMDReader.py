import unittest

import LazyAMDReader

class TestReader(unittest.TestCase): 

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

#TODO: Add tests for filter_for_slice_uri

if __name__ == '__main__':
	unittest.main() #unittest.main

