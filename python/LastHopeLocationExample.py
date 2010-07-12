#!/usr/bin/env python
import networkx as nx
import csv
import matplotlib.pylab as plt
import os.path

## Example by Rob Zinkov
## minor updates by Far McKon

def load_location_graph():
	reader = csv.reader(file("../data/position_snapshot.csv"))
	headers = reader.next()

	last_time = ""

	zones = {}
	edges = {}
	nodes = {}

	for line in reader:
		nodes[line[1]] = nodes.get(line[1],0)+1
		if line[0] != last_time:
			for z in zones:
				for i in zones[z]:
					for j in filter(lambda x: x!=i,zones[z]):
						edges[(i,j)] = edges.get((i,j),0)+1
						edges[(j,i)] = edges.get((j,i),0)+1                       
			last_time = line[0]
			zones = {}
		else:
			zones[line[2]] = zones.get(line[2],set()).union([line[1]])
	G = nx.Graph()
	for (e1,e2) in edges:
		weight = edges[(e1,e2)]/(nodes[e1]+nodes[e2]-edges[(e1,e2)])
		#alternative weight
		# weight = edges[(e1,e2)]/min(nodes[e1],nodes[e2])
		if weight > 0.08:
			G.add_edge(e1,e2,weight=weight)
	print "Nodes:%d Edges: %d\n" % (len(G.nodes()),len(G.edges()))

	pos = nx.spring_layout(G,weighted=True)     
	nx.draw(G,
			pos,
			node_size=40,
			with_labels=False,
			alhpa = 0.5,
			node_color=[float(G.degree(v)) for v in G],
			cmap=plt.cm.Greens,
			)
	plt.show()

if __name__ == "__main__":

	if not os.path.exists("../data/position_snapshot.csv"):
		print "please download the Last Hope data set unto the same directory as this file"
		print "the last hope data set can be found at http://crawdad.org/meta.php?name=hope/amd "	
	else :
		show_ping_graph()
	
