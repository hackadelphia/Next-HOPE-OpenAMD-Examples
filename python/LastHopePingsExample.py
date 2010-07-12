#!/usr/bin/env python
import networkx as nx
import csv
import matplotlib.pylab as plt
import os.path

## Example by Rob Zinkov
## minor updates by Far McKon


def show_ping_graph():
	reader = csv.reader(file("ping.csv"))
	headers = reader.next()
	
	G = nx.Graph()
	
	for line in reader:
		G.add_edge(line[0],line[1])
	
		nx.draw_spring(G,
					   node_color=[float(G.degree(v)) for v in G],
					   node_size=40,
					   with_labels=False,
					   cmap=plt.cm.Reds,
					   )
	plt.show()
	
if __name__ == "__main__":

	if not os.path.exists("ping.csv"):
		print "please download the Last Hope data set unto the same directory as this file"
		print "the last hope data set can be found at http://crawdad.org/meta.php?name=hope/amd "	
	else :
		show_ping_graph()
	
