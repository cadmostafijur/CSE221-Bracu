def BFS(G, s):
    visited = []
    Q = []
    path = []
    visited.append(s)
    Q.append(s)
    while Q:
        x = Q.pop(0)
        path.append(x)
        for j in G[x]:
            if j not in visited:
                visited.append(j)
                Q.append(j)
    return path
file1 = open("input2.txt", "r")
file2 = open("output2.txt", "w")
lines = file1.read().split("\n")
N, M = map(int, lines[0].split())
G = {i:[] for i in range(N+1)}
for i in range(1, len(lines), 1):
  info = lines[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = G[node1]
  arr.append(node2)
path = BFS(G, 1)
file2.write(" ".join(list(map(str, path))))
file2.close()

#========== Task 2  ==========#
# We have an undirected, unweighted graph that we need to find a way 
# through. Within the BFS function, there is a viewed array and a 
# queue away array. When we find a mode that hasn't been seen before,
# we add a node to the visited list. The newly viewed modes are in 
# the queue. Although the list isn't empty, we take a node from it 
# and add it to the path array. Afterwards, we add the node's peers
# to the visited array and check to see if it has been visited yet. 
# This will keep going until the whole line has been gone through.