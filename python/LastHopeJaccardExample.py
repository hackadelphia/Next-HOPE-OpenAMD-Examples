#!/usr/bin/env python
import networkx as nx
import csv
import matplotlib.pylab as plt
import os.path


## Example by Rob Zinkov
## minor updates by Far McKon



def jaccard(a, b):
	c = a.intersection(b)
	return float(len(c)) / (len(a) + len(b) - len(c))

def show_talk_graph():
	reader = csv.reader(file("talk_presence.csv"))
	headers = reader.next()

	talks_seen = {}
	G = nx.Graph()

	for line in reader:
		if line[0] not in talks_seen:
			talks_seen[line[0]] = set(line[1])
		else: talks_seen[line[0]].add(line[1])
	for t in talks_seen:
		for u in talks_seen:
			if t is not u:
				weight = jaccard(talks_seen[t],
								 talks_seen[u])
				if weight > 0.4:                
					G.add_edge(t,u,weight=weight)
	pos = nx.spring_layout(G,weighted=True)     
	nx.draw(G,
			pos,
			edge_color=[float(G[e1][e2]['weight']+0.1) for e1,e2 in G.edges()],
			width=4,
			node_size=40,
			edge_cmap=plt.cm.Blues,
			with_labels=False,

			node_color=[float(G.degree(v)) for v in G],
			cmap=plt.cm.Blues,
			)
	print "Nodes:%d Edges: %d\n" % (len(G.nodes()),len(G.edges()))
	plt.show()

if __name__ == "__main__":

	if not os.path.exists("talk_presence.csv"):
		print "please download the Last Hope data set unto the same directory as this file"
		print "the last hope data set can be found at http://crawdad.org/meta.php?name=hope/amd "	
	else :
		show_talk_graph()
