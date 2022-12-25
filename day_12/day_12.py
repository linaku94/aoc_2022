import numpy as np 
import networkx as nx 

my_map = []
N, M = 0,0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        N+=1
        for letter in line:
            if letter.islower():
                my_map.append(ord(letter)-97)
            elif letter == 'S':
                start = len(my_map)
                my_map.append(0)
            else:
                end = len(my_map)
                my_map.append(ord('z')-97)
            M+=1

M = M//N
my_map = np.array(my_map).reshape((N,M))
G = nx.grid_2d_graph(N, M, create_using=nx.DiGraph)
removals = []
for edge in G.edges:
    n0, n1 = edge[0], edge[1]
    if my_map[n1]-my_map[n0] >1:
        removals.append((n0, n1))
for r in removals:
    G.remove_edge(*r)

end = (end//M, end%M)
start = (start//M, start%M)
path = nx.astar_path(G, start, end)
print(f"part 1 pathlength: {len(path)-1}")

shortes_path = len(G.nodes)
for node in G.nodes:
    if my_map[node] == 0:
        start = node
        try:
            path = nx.astar_path(G, start, end)
            shortes_path=min(len(path)-1, shortes_path)
        except:
            continue
print(f"part 2 shortes_path: {shortes_path}")
