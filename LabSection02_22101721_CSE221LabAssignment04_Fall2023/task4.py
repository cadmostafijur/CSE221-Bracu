def DFS(G,u,visited,stack):
    visited[u] = True
    stack[u] = True
    for v in G[u]:
        if not visited[v]:
            if DFS(G,v,visited,stack):
                return True
        elif stack[v]:
            return True
    stack[u] = False
    return False
def isCycle(G):
    for u in range(len(G)):
        if DFS(G,u,visited,stack):
            return True

    return False
file1 = open("input4.txt", "r")
file2 = open("output4.txt", "w")
lines = file1.read().split("\n")
N, M = map(int, lines[0].split())
G = {i:[] for i in range(N+1)}
for i in range(1, len(lines), 1):
  info = lines[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  arr = G[node1]
  arr.append(node2)
visited = [False] * (N+1)
stack = [False] * (N+1)
if isCycle(G)==True:
  file2.write("YES")
else:
  file2.write("NO")
file2.close()


#========== Task 4  ==========#
# The iscycle function calls the dfs function for every
# node in the graph. The dfs graph function maintains
# two arrays  visited (the overall visited nodes) and
# the stack (nodes found in current traversal), for every
# neighbour of the node, the dfs function is recursively.
# called if it is not visited. This is to check if a cycle
# exists and if it possible to go back to the original
# node from another node. After each node is checked,
# the node is  not included in the stack. If a
# cycle is detected, the dfs function returns True, which
# causes the iscycle function to also return True.