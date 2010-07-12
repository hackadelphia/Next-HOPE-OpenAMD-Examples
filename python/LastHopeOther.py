
def print_cliques():

    cliques = sorted(nx.find_cliques(G),key=len,reverse=True)[:10]
    for c in cliques:
        c = filter(lambda x: name[x] is not "",c)
        print map(lambda x: name[x], c)
        

def print_reachable():        
    parts = nx.connected_components(G)
    for p in parts[:10]:
        p = filter(lambda x: name[x] is not "",p)
        print map(lambda x: name[x], p)
     