def shortestPath(G, start, end):
    p_list = [[start]] #path list start
    visited = [start]
    if start == end:
        return [start]
    while len(p_list)>0:
        currentPath = p_list[0]
        lastNode = currentPath[-1]
        p_list.pop(0)
        nextNodes = G[lastNode]
        if end in nextNodes:
            currentPath.append(end)
            return currentPath
        for node in nextNodes:
            if not node in visited:
                newPath = list(currentPath)
                newPath.append(node)
                p_list.append(newPath)
                visited.append(node)
    return []
file1 = open("input5.txt", "r")
file2 = open("output5.txt", "w")
lines = file1.read().split("\n")
N, M, E = map(int, lines[0].split())
G = {i:[] for i in range(N+1)}
for i in range(1, len(lines), 1):
  info = lines[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = G[node1]
  arr.append(node2)
  arr = G[node2]
  arr.append(node1)
path = shortestPath(G, 1, E)
file2.write("Time: "+str(len(path)-1)+"\n")
file2.write("Shortest Path: "+" ".join(list(map(str, path))))
file2.close()

#========== Task 5 ==========#
# Here, we find every path possible to take from the 
# Starting point and check if the end node is reached.
# There are two arrays path list (holds all possible paths),
# visited (holds previously visited nodes to prevent backtracking).
# For every path list, we take the last node, get all its children and 
# check if the end node is among there. If not and if the node is unvisited,
# a new path is added to path list containing the previous path and this node added.
# It is also set an visited. In this way, we check paths till we find the Shortest one.
# time is just number one of nodes -1.